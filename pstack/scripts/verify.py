#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import re
import sys


def verify(root):
    lock = json.loads((root / "upstream.lock.json").read_text())
    errors = []
    snapshot = root / lock["snapshot"]
    expected_files = set(lock["files"])
    actual_files = {
        path.relative_to(snapshot).as_posix()
        for path in snapshot.rglob("*") if path.is_file()
    }
    if actual_files != expected_files:
        errors.append(f"Snapshot file set changed: {actual_files ^ expected_files}")
    for name, recorded in lock["files"].items():
        path = snapshot / name
        if not path.is_file():
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != recorded["sha256"]:
            errors.append(f"Snapshot content changed: {name}")
        if bool(path.stat().st_mode & 0o111) != recorded["executable"]:
            errors.append(f"Snapshot executable mode changed: {name}")
        if path.is_symlink():
            errors.append(f"Unexpected snapshot symlink: {name}")

    source_names = {path.parent.name for path in (snapshot / "skills").glob("*/SKILL.md")}
    if source_names != set(lock["commands"]):
        errors.append("Command map does not cover exactly the upstream public skills")
    entries = {item["name"]: item for item in lock["commands"].values()}
    for alias in lock["aliases"]:
        entries[alias] = {"path": f"skills/{alias}", "allow_implicit_invocation": True}
    if set(path.name for path in (root / "skills").iterdir()) != set(entries):
        errors.append("Local entrypoints differ from the command map")

    discovery = (root.parent / "skills" if root.parent.name == ".agents"
                 else root.parent / ".agents" / "skills")
    for name, entry in entries.items():
        folder = root / entry["path"]
        manifest = folder / "SKILL.md"
        if not manifest.is_file():
            errors.append(f"Missing entrypoint: {name}")
            continue
        content = manifest.read_text()
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"Invalid skill name: {name}")
        if f"\nname: {name}\n" not in content:
            errors.append(f"Entrypoint name does not match folder: {name}")
        if "../../codex.md" not in content:
            errors.append(f"Entrypoint does not load the adapter: {name}")
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if "://" not in target and not (folder / target.split("#")[0]).exists():
                errors.append(f"Broken entrypoint reference: {name}: {target}")
        metadata = folder / "agents" / "openai.yaml"
        if not metadata.is_file():
            errors.append(f"Missing Codex metadata: {name}")
        else:
            expected_policy = entry["allow_implicit_invocation"]
            match = re.search(r"allow_implicit_invocation: (true|false)", metadata.read_text())
            actual_policy = match is None or match[1] == "true"
            if actual_policy != expected_policy:
                errors.append(f"Invocation policy changed: {name}")
        link = discovery / name
        if link.is_symlink():
            if link.resolve() != folder.resolve():
                errors.append(f"Incorrect discovery link: {name}")
        elif link.is_dir():
            for path in folder.rglob("*"):
                if not path.is_file():
                    continue
                relative = path.relative_to(folder)
                installed = link / relative
                expected = path.read_bytes()
                if relative.as_posix() == "SKILL.md":
                    expected = expected.replace(b"](../../", b"](../../pstack/")
                if not installed.is_file() or installed.read_bytes() != expected:
                    errors.append(f"Incorrect installed entrypoint: {name}/{relative}")
        else:
            errors.append(f"Missing discovery entrypoint: {name}")

    exposed = {path.name for path in discovery.glob("pstack*")}
    if exposed != set(entries):
        errors.append(f"Unexpected discovery set: {exposed ^ set(entries)}")
    return errors, len(expected_files), len(entries)


if __name__ == "__main__":
    errors, file_count, skill_count = verify(Path(__file__).resolve().parents[1])
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print(f"PASS: {file_count} unchanged upstream files; {skill_count} discoverable entrypoints.")

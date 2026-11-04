#!/usr/bin/env python3
"""Import or verify the published Matt Pocock skills at a fixed Git commit."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "imports/mattpocock.lock.json"
SOURCE = "https://github.com/mattpocock/skills"


def fingerprint(data, executable=False):
    return {"sha256": hashlib.sha256(data).hexdigest(), "executable": executable}


def verify(skills_root, lock):
    count = 0
    for name, skill in lock["skills"].items():
        folder = skills_root / name
        if not folder.is_dir():
            raise ValueError(f"Missing skill: {name}")
        paths = list(folder.rglob("*"))
        if any(path.is_symlink() for path in paths):
            raise ValueError(f"Unexpected symlink inside skill: {name}")
        files = {path.relative_to(folder).as_posix(): path for path in paths if path.is_file()}
        if set(files) != set(skill["files"]):
            raise ValueError(f"File set changed: {name}")
        for relative, expected in skill["files"].items():
            path = files[relative]
            if fingerprint(path.read_bytes(), bool(path.stat().st_mode & 0o111)) != expected:
                raise ValueError(f"Imported content or executable mode changed: {name}/{relative}")
            count += 1
    return count


def import_skills(checkout, revision):
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Use a full 40-character Git commit SHA.")

    def git(*args):
        return subprocess.check_output(["git", "-C", str(checkout), *args])

    if git("rev-parse", f"{revision}^{{commit}}").decode().strip() != revision:
        raise ValueError("Revision must identify a commit directly.")
    plugin_path = ".claude-plugin/plugin.json"
    plugin = json.loads(git("show", f"{revision}:{plugin_path}"))
    if not plugin.get("skills"):
        raise ValueError("The upstream plugin must publish at least one skill.")
    license_data = git("show", f"{revision}:LICENSE")
    lock = {
        "repository": SOURCE,
        "revision": revision,
        "selection": f"{plugin_path}#skills",
        "license": {"source": "LICENSE", "sha256": fingerprint(license_data)["sha256"]},
        "skills": {},
    }
    contents = {}
    for source in sorted(plugin["skills"]):
        source = source.removeprefix("./")
        if not re.fullmatch(r"skills/(engineering|productivity)/[a-z0-9-]+", source):
            raise ValueError(f"Review the newly published skill category before importing: {source}")
        name = source.rsplit("/", 1)[1]
        if name in lock["skills"]:
            raise ValueError(f"Duplicate upstream skill name: {name}")
        files = {}
        tree = git("ls-tree", "-rz", revision, "--", source)
        for record in tree.split(b"\0"):
            if not record:
                continue
            header, filename = record.decode().split("\t", 1)
            mode, kind, _ = header.split()
            if kind != "blob" or mode not in ("100644", "100755"):
                raise ValueError(f"Unsupported upstream file mode: {filename}")
            relative = filename.removeprefix(source + "/")
            data = git("show", f"{revision}:{filename}")
            files[relative] = fingerprint(data, mode == "100755")
            contents[(name, relative)] = data
        manifest = contents.get((name, "SKILL.md"), b"").decode()
        if not re.search(rf"^name: {re.escape(name)}$", manifest, re.MULTILINE):
            raise ValueError(f"Upstream skill name differs from its directory: {source}")
        if "agents/openai.yaml" not in files:
            raise ValueError(f"Missing upstream Codex metadata: {source}")
        if "LICENSE" not in files:
            files["LICENSE"] = fingerprint(license_data)
            contents[(name, "LICENSE")] = license_data
        lock["skills"][name] = {"source": source, "files": dict(sorted(files.items()))}

    previous = json.loads(LOCK.read_text()) if LOCK.exists() else {"skills": {}}
    verify(ROOT / "skills", previous)
    for name in lock["skills"]:
        destination = ROOT / "skills" / name
        if name not in previous["skills"] and (destination.exists() or destination.is_symlink()):
            raise ValueError(f"Refusing to replace an existing skill: {name}")
    for name in previous["skills"]:
        shutil.rmtree(ROOT / "skills" / name)
    for (name, relative), data in contents.items():
        destination = ROOT / "skills" / name / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        destination.chmod(0o755 if lock["skills"][name]["files"][relative]["executable"] else 0o644)
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    LOCK.write_text(json.dumps(lock, indent=2) + "\n")
    return lock


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--import-from", type=Path, help="Local upstream Git checkout; reads committed files only")
    parser.add_argument("--revision", help="Full upstream commit SHA; required for import")
    parser.add_argument("--skills-root", type=Path, default=ROOT / "skills", help="Skill directory to verify")
    args = parser.parse_args()
    if bool(args.import_from) != bool(args.revision):
        parser.error("Use --import-from and --revision together.")
    if args.import_from and args.skills_root != ROOT / "skills":
        parser.error("--skills-root is only available when verifying.")
    try:
        lock = import_skills(args.import_from, args.revision) if args.import_from else json.loads(LOCK.read_text())
        count = verify(args.skills_root, lock)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"{error}\n")
    print(f"PASS: {len(lock['skills'])} Matt Pocock skills; {count} pinned files; revision {lock['revision']}.")


if __name__ == "__main__":
    main()

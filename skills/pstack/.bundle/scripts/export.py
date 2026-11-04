#!/usr/bin/env python3
"""Generate committed skill folders for the standard skills CLI."""

import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True


def entrypoints(lock):
    entries = {item["name"]: item for item in lock["commands"].values()}
    for alias in lock["aliases"]:
        entries[alias] = {"path": f"skills/{alias}", "allow_implicit_invocation": True}
    return entries


def exported_files(root, name, entry):
    source = root / entry["path"]
    manifest = (source / "SKILL.md").read_text()
    if name == "pstack":
        manifest = manifest.replace("](../../", "](.bundle/")
        manifest = manifest.replace("](../", "](.bundle/skills/")
    else:
        manifest = manifest.replace("](../../", "](../pstack/.bundle/")
        manifest = manifest.replace("in `../`", "in `../pstack/.bundle/skills/`")
        marker = "1. Read [the Codex adapter]"
        requirement = (
            "This entrypoint requires the `pstack` skill alongside it. If\n"
            "`../pstack/.bundle/codex.md` is missing, stop and ask to install `pstack`\n"
            "from the same reviewed revision.\n"
            "Do not fetch or install dependencies during a workflow.\n\n"
        )
        manifest = manifest.replace(marker, requirement + marker)
    return {
        "SKILL.md": manifest.encode(),
        "agents/openai.yaml": (source / "agents/openai.yaml").read_bytes(),
    }


def main():
    root = Path(__file__).resolve().parents[1]
    repository = root.parent.parent.parent
    package = repository / "package.json"
    if (
        not package.is_file()
        or json.loads(package.read_text()).get("name") != "@fahu/skills"
    ):
        sys.exit("Generate exports in the fahu/skills repository, not an installed skill.")
    lock = json.loads((root / "upstream.lock.json").read_text())
    entries = entrypoints(lock)
    for name, entry in entries.items():
        for relative, content in exported_files(root, name, entry).items():
            destination = root.parent.parent / name / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
    print(f"Generated {len(entries)} pstack skill exports.")


if __name__ == "__main__":
    main()

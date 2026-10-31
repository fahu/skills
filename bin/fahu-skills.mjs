#!/usr/bin/env node
import { createHash } from "node:crypto";
import * as fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const packageRoot = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const groups = ["pstack", "commits", "github-pr-management"];
const help = `Usage: fahu-skills install [--target DIRECTORY] [--only GROUP]

Install project-local Codex skills without overwriting existing files.
GROUP is pstack, commits, or github-pr-management; the default is all groups.
DIRECTORY defaults to the current directory and must already exist.
Repeated installation of identical contents is a no-op.
`;

async function statOrNull(filename) {
  try {
    return await fs.lstat(filename);
  } catch (error) {
    if (error.code === "ENOENT") return null;
    throw error;
  }
}

async function readTree(directory, prefix = "") {
  const files = new Map();
  for (const entry of await fs.readdir(directory, { withFileTypes: true })) {
    const relative = path.posix.join(prefix, entry.name);
    const filename = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      for (const [name, value] of await readTree(filename, relative)) files.set(name, value);
    } else if (entry.isFile()) {
      files.set(relative, {
        data: await fs.readFile(filename),
        mode: (await fs.stat(filename)).mode & 0o777,
      });
    } else {
      throw new Error(`Unsupported file or symlink: ${filename}`);
    }
  }
  return files;
}

function sameTree(first, second) {
  return first.size === second.size && [...first].every(([name, value]) => {
    const other = second.get(name);
    return other && value.data.equals(other.data)
      && Boolean(value.mode & 0o111) === Boolean(other.mode & 0o111);
  });
}

async function checkParents(target, relative) {
  let current = target;
  for (const component of relative.split("/")) {
    current = path.join(current, component);
    const stat = await statOrNull(current);
    if (stat && (!stat.isDirectory() || stat.isSymbolicLink())) {
      throw new Error(`Refusing non-directory or symlink destination: ${current}`);
    }
  }
}

async function makePlan(selected) {
  const plan = new Map();
  if (selected.includes("pstack")) {
    const files = await readTree(path.join(packageRoot, "pstack"));
    const npmFiles = JSON.parse(await fs.readFile(path.join(packageRoot, "bin/npm-files.json")));
    for (const [name, content] of Object.entries(npmFiles)) {
      if (!files.has(name)) files.set(name, { data: Buffer.from(content), mode: 0o644 });
    }
    const lock = JSON.parse(files.get("upstream.lock.json").data);
    const snapshotFiles = [...files.keys()].filter(name => name.startsWith("upstream/"));
    if (snapshotFiles.length !== Object.keys(lock.files).length) {
      throw new Error("Incomplete pstack snapshot in npm package");
    }
    for (const [name, expected] of Object.entries(lock.files)) {
      const file = files.get(`upstream/${name}`);
      if (!file || createHash("sha256").update(file.data).digest("hex") !== expected.sha256
        || Boolean(file.mode & 0o111) !== expected.executable) {
        throw new Error(`pstack snapshot integrity failed: ${name}`);
      }
    }
    plan.set(".agents/pstack", files);
    const names = [...Object.values(lock.commands).map(command => command.name), ...Object.keys(lock.aliases)];
    for (const name of names) {
      const prefix = `skills/${name}/`;
      const wrapper = new Map();
      for (const [filename, file] of files) {
        if (!filename.startsWith(prefix)) continue;
        const relative = filename.slice(prefix.length);
        wrapper.set(relative, relative === "SKILL.md"
          ? { ...file, data: Buffer.from(file.data.toString().replaceAll("](../../", "](../../pstack/")) }
          : file);
      }
      if (!wrapper.has("SKILL.md")) throw new Error(`Missing pstack entrypoint: ${name}`);
      plan.set(`.agents/skills/${name}`, wrapper);
    }
  }
  for (const name of selected.filter(name => name !== "pstack")) {
    plan.set(`.agents/skills/${name}`, await readTree(path.join(packageRoot, name)));
  }
  return plan;
}

async function install(target, selected) {
  target = await fs.realpath(target);
  if (!(await fs.stat(target)).isDirectory()) throw new Error(`Not a directory: ${target}`);
  const plan = await makePlan(selected);
  const pending = [];
  for (const [relative, files] of plan) {
    await checkParents(target, relative);
    const destination = path.join(target, relative);
    if (await statOrNull(destination)) {
      if (!sameTree(files, await readTree(destination))) {
        throw new Error(`Refusing to overwrite existing content: ${destination}`);
      }
    } else {
      pending.push([destination, files]);
    }
  }

  const created = [];
  try {
    for (const [destination, files] of pending) {
      await checkParents(target, path.relative(target, destination).split(path.sep).join("/"));
      await fs.mkdir(path.dirname(destination), { recursive: true });
      await fs.mkdir(destination);
      created.push(destination);
      for (const [name, file] of files) {
        const filename = path.join(destination, name);
        await fs.mkdir(path.dirname(filename), { recursive: true });
        await fs.writeFile(filename, file.data, { flag: "wx", mode: file.mode });
        await fs.chmod(filename, file.mode);
      }
    }
  } catch (error) {
    for (const directory of created.reverse()) await fs.rm(directory, { recursive: true });
    throw error;
  }
  const count = [...plan.keys()].filter(name => name.startsWith(".agents/skills/")).length;
  console.log(`${pending.length ? "Installed" : "Already installed"} ${count} skills in ${target}`);
}

try {
  const args = process.argv.slice(2);
  if (args.length === 0 || (args.length === 1 && ["--help", "-h"].includes(args[0]))) {
    console.log(help);
  } else {
    if (args.shift() !== "install") throw new Error(help);
    let target = process.cwd();
    let selected = groups;
    const seen = new Set();
    while (args.length) {
      const option = args.shift();
      if (!["--target", "--only"].includes(option) || seen.has(option)) {
        throw new Error(`Unknown or repeated option: ${option}\n${help}`);
      }
      seen.add(option);
      const value = args.shift();
      if (!value || value.startsWith("--")) throw new Error(`Missing value for ${option}`);
      if (option === "--target") target = path.resolve(value);
      else {
        if (!groups.includes(value)) throw new Error(`Unknown group: ${value}`);
        selected = [value];
      }
    }
    await install(target, selected);
  }
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}

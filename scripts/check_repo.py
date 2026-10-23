"""Check repository documentation and private-data tracking boundaries.

Python 3.9+ and Git only. This is not an application test or a secret scanner.
Ignored personal data is not opened. Run from any directory.
"""

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md",
    "AGENT.md",
    "README.md",
    ".gitignore",
    "docs/INDEX.md",
    "docs/STATUS.md",
    "docs/architecture/current-architecture.md",
    "docs/decisions/0002-open-notebook-base.md",
    "docs/development/repository-layout.md",
    "docs/development/git-workflow.md",
    "data/README.md",
    "outputs/README.md",
)
LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+[\"'][^\n]*?[\"'])?\s*\)")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
DATABASE = re.compile(r"\.(?:db|sqlite|sqlite3)(?:-.*)?$", re.IGNORECASE)


def git_paths(*args):
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-z", *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return {name for name in result.stdout.decode("utf-8").split("\0") if name}


def visible_markdown(text):
    """Blank fenced code but retain line numbers for useful diagnostics."""
    fence = None
    lines = []
    for line in text.splitlines(keepends=True):
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            lines.append("\n")
        elif fence:
            lines.append("\n")
        else:
            lines.append(line)
    return "".join(lines)


def private_path(name):
    parts = name.split("/")
    basename = parts[-1]
    if parts[0] in {"data", "outputs"}:
        return name not in {"data/README.md", "outputs/README.md"}
    if any(part in {".git", "node_modules", ".venv", "__pycache__"} for part in parts):
        return True
    if parts[0] in {"_scratch", "logs"} or name.startswith("config/local/"):
        return True
    if basename == ".env" or (basename.startswith(".env.") and not basename.endswith(".example")):
        return True
    return bool(DATABASE.search(basename)) or Path(basename).suffix.lower() in {
        ".pem", ".key", ".p12", ".pfx", ".log", ".safetensors", ".ckpt",
    }


def main():
    try:
        tracked = git_paths("--cached")
        candidates = tracked | git_paths("--others", "--exclude-standard")
    except (OSError, subprocess.CalledProcessError) as exc:
        print("ERROR: Git could not list repository files: {}".format(exc), file=sys.stderr)
        return 2

    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append("Missing required file: " + name)
    for name in sorted(candidates):
        if private_path(name):
            errors.append("Private/runtime file must not be versioned: " + name)

    # A nested Git checkout can otherwise look like an ordinary source directory.
    submodules = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--stage"],
        check=True, stdout=subprocess.PIPE, encoding="utf-8",
    ).stdout
    for line in submodules.splitlines():
        if line.startswith("160000 "):
            errors.append("Nested repository/gitlink is not allowed: " + line.split("\t", 1)[-1])

    checked_docs = 0
    checked_links = 0
    for name in sorted(candidates):
        path = ROOT / name
        if private_path(name) or path.suffix.lower() != ".md" or not path.is_file():
            continue
        try:
            contents = visible_markdown(path.read_text(encoding="utf-8-sig"))
        except (OSError, UnicodeError) as exc:
            errors.append("Cannot read {}: {}".format(name, exc))
            continue
        checked_docs += 1
        for match in LINK.finditer(contents):
            target = match.group(1).strip("<>")
            if target.startswith(("#", "//")) or SCHEME.match(target):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            checked_links += 1
            resolved = ROOT / target.lstrip("/") if target.startswith("/") else path.parent / target
            if not resolved.exists():
                line = contents.count("\n", 0, match.start()) + 1
                errors.append("{}:{}: missing link target {}".format(name, line, target))

    if errors:
        print("Repository checks FAILED:")
        for error in errors:
            print("- " + error)
        return 1
    print("Repository checks passed: {} Markdown files, {} local links; no private/runtime files in the versionable file list.".format(checked_docs, checked_links))
    print("Scope: file targets and tracking boundaries only; no application, semantic, or secret-content validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

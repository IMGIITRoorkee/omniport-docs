"""
Check that every path declared in a :sourcefiles: field still exists.

Run it from the repository root. Needs no clones; it asks GitHub. Set
GITHUB_TOKEN, or be logged in to the gh CLI, to raise the rate limit.
"""

import os
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

ORG = 'IMGIITRoorkee'
BRANCH = 'master'
FIELD = re.compile(r'\A:sourcefiles:\n((?:[ \t]+\S+\n)+)', re.MULTILINE)


def token():
    if os.environ.get('GITHUB_TOKEN'):
        return os.environ['GITHUB_TOKEN']
    try:
        found = subprocess.run(
            ['gh', 'auth', 'token'], capture_output=True, text=True, timeout=10
        )
        return found.stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


def declared(root):
    for path in sorted(pathlib.Path(root).rglob('*.rst')):
        match = FIELD.search(path.read_text(encoding='utf-8'))
        if match:
            for entry in match.group(1).split():
                yield path, entry


def exists(entry, auth):
    """True if present, False if absent, and never a guess in between."""

    repo, _, path = entry.partition('/')
    url = f'https://api.github.com/repos/{ORG}/{repo}/contents/{path}?ref={BRANCH}'
    request = urllib.request.Request(url)
    if auth:
        request.add_header('Authorization', f'Bearer {auth}')
    try:
        urllib.request.urlopen(request, timeout=30).read()
        return True
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return False
        raise SystemExit(
            f'GitHub answered {error.code} for {entry}. That is not an answer '
            f'about the file, so nothing is being reported as missing.'
        )


def main():
    auth = token()
    missing = [
        (page, entry)
        for page, entry in declared('docs/source')
        if not exists(entry, auth)
    ]
    for page, entry in missing:
        print(f'{page}: {entry} no longer exists')
    print(f'{len(missing)} missing')
    return 1 if missing else 0


if __name__ == '__main__':
    sys.exit(main())

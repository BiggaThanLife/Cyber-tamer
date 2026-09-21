"""Copy BUILD (version, date, notes) from index.html into version.json.

The game polls version.json to tell players an update is out. Run this after
bumping BUILD in index.html, then commit both files:

    python tools/sync_version.py
"""
import json, re, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
html = (root / 'index.html').read_text(encoding='utf-8')
m = re.search(r"const BUILD = \{(.*?)\n  \};", html, re.S)
if not m:
    sys.exit('BUILD block not found in index.html')
block = m.group(1)
str_re = r"'((?:[^'\\]|\\.)*)'"
version = re.search(r"version:\s*" + str_re, block).group(1)
date = re.search(r"date:\s*" + str_re, block).group(1)
notes_block = re.search(r"notes:\s*\[(.*?)\n    \]", block, re.S).group(1)
notes = [n.replace("\\'", "'") for n in re.findall(str_re, notes_block)]
data = {'version': version, 'date': date, 'notes': notes}
(root / 'version.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('version.json ->', version, f'({len(notes)} notes)')

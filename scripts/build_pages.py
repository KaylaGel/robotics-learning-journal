"""Prepare the GitHub Pages source from the journal's Markdown documents."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
SOURCES = [ROOT / 'README.md', ROOT / 'ROADMAP.md']
for folder in ('guides', 'projects', 'journal', 'resources', 'templates'):
    SOURCES.extend(sorted((ROOT / folder).rglob('*.md')))

def destination(source):
    relative = source.relative_to(ROOT)
    if relative.name == 'README.md':
        return relative.with_name('index.md')
    return relative

for source in SOURCES:
    target = DOCS / destination(source)
    text = source.read_text()
    title = text.splitlines()[0].removeprefix('# ')
    def link(match):
        label, url = match.groups()
        if '://' in url or url.startswith('#'):
            return match.group(0)
        path, separator, fragment = url.partition('#')
        if path.endswith('.md'):
            path = str(Path(path).with_name('index.md')) if Path(path).name == 'README.md' else path
            path = path[:-3] + '.html'
        return f'[{label}]({path}{separator}{fragment})'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, text)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('---\nlayout: default\ntitle: "' + title.replace('"', '\\"') + '"\n---\n\n' + text)
print(f'Prepared {len(SOURCES)} pages in docs/')

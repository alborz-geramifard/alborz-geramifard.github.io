"""Build notes.html from data/notes.json (LinkedIn articles written by the author)."""
import json, html, os, datetime
ROOT = os.path.join(os.path.dirname(__file__), '..')
A = json.load(open(os.path.join(ROOT, 'data', 'notes.json')))
A.sort(key=lambda a: a['date'], reverse=True)
e = html.escape
def nice(d): return datetime.date.fromisoformat(d).strftime('%b %-d, %Y')
out = []; year = None
for a in A:
    y = a['date'][:4]
    if y != year:
        if year: out.append('  </ol>\n</section>')
        out.append(f'<section class="post-year">\n  <h2>{y}</h2>\n  <ol class="posts">'); year = y
    cover = f'<img src="{e(a["cover"])}" alt="" loading="lazy">' if a.get('cover') else '<div class="nocover"></div>'
    read = f'<span class="rt">{e(a["read"])}</span>' if a.get('read') else ''
    out.append(f'''    <li class="post">
      <time datetime="{a['date']}">{nice(a['date'])}{read}</time>
      <a class="note-card" href="{e(a['url'])}" target="_blank" rel="noopener">
        <div class="note-cover">{cover}</div>
        <div class="note-body">
          <h3>{e(a['title'].strip())}</h3>
          <p>{e(a.get('desc') or '')}</p>
          <span class="note-cta">Read on LinkedIn ↗</span>
        </div>
      </a>
    </li>''')
out.append('  </ol>\n</section>')
tmpl = open(os.path.join(os.path.dirname(__file__), 'notes.tmpl.html')).read()
open(os.path.join(ROOT, 'notes.html'), 'w').write(tmpl.replace('<!--NOTES-->', '\n'.join(out)))
print(len(A), 'notes')

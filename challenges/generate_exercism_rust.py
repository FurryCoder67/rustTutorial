import os
import re
import urllib.request

ROOT = os.path.dirname(__file__)
BASE_DIR = os.path.join(ROOT)
URL = 'https://exercism.org/tracks/rust/exercises'

def fetch_page(url):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (compatible; exercism-fetcher/1.0)'
    })
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode('utf-8')

def safe_mkdir(path):
    os.makedirs(path, exist_ok=True)


def make_files(difficulty, slug, name, link):
    folder = os.path.join(BASE_DIR, difficulty, slug)
    safe_mkdir(folder)
    # README.md
    readme = f"""# {name}

Exercise from Exercism: {link}

Difficulty: {difficulty.capitalize()}

## Task

Implement the exercise as described on Exercism.

## Files

"""
    with open(os.path.join(folder, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme)
    # workspace.rs
        workspace = """// Exercise: {name}
    // Slug: {slug}

    pub fn solve() {{
        todo!("implement {slug}")
    }}
    """.format(name=name, slug=slug)
    with open(os.path.join(folder, 'workspace.rs'), 'w', encoding='utf-8') as f:
        f.write(workspace)
    # solution.rs
    solution = f"// Solution placeholder for {name}\n\n// Implemented solution should go here.\n\n"
    with open(os.path.join(folder, 'solution.rs'), 'w', encoding='utf-8') as f:
        f.write(solution)


def main():
    print('Fetching exercise list...')
    html = fetch_page(URL)
    # Find all exercise links
    pattern = re.compile(r'/tracks/rust/exercises/([a-z0-9\-]+)', re.IGNORECASE)
    matches = pattern.findall(html)
    # matches is a list of slugs
    seen = set()
    entries = []
    for slug in matches:
        if slug in seen:
            continue
        seen.add(slug)
        full = '/tracks/rust/exercises/' + slug
        idx = html.find(full)
        snippet = html[idx: idx+400] if idx != -1 else ''
        diff_match = re.search(r"(Easy|Medium|Hard)", snippet)
        difficulty = diff_match.group(1).lower() if diff_match else 'medium'
        # fallback name
        name = slug.replace('-', ' ').title()
        link = 'https://exercism.org' + full
        entries.append((difficulty, slug, name, link))

    print(f'Found {len(entries)} exercises; creating files...')
    for difficulty, slug, name, link in entries:
        make_files(difficulty, slug, name, link)
    print('Done. Created exercise folders under', BASE_DIR)

if __name__ == '__main__':
    main()

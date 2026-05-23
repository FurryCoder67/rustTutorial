import re
import os

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
changed = []

replacements = {
    r'is dedicated to': 'Focuses on',
    r'is focused on': 'Focuses on',
    r'is the introduction to': 'Introduces',
    r'dives into': 'Explores',
    r'introduces': 'Introduces',
    r'explains': 'Explains',
    r'covers': 'Covers',
    r'contains': 'Contains',
    r'teaches': 'Teaches',
    r'is about': 'Covers'
}

pattern = re.compile(r"This folder (" + "|".join(replacements.keys()) + r")", re.IGNORECASE)

for dirpath, dirnames, filenames in os.walk(root):
    for fname in filenames:
        if fname.lower() == 'readme.md':
            path = os.path.join(dirpath, fname)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            new_text = pattern.sub(lambda m: replacements[m.group(1).lower()], text)
            if new_text != text:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_text)
                changed.append(path)

print(f'Updated {len(changed)} README files')
for p in changed:
    print(p)

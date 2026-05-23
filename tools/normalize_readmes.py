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
            # Normalize lead-in learning outcome headings to a consistent '## Learning outcomes'
            new_text = re.sub(r'(?m)^(From this folder, you should learn:|After reading this folder, you should understand:|After studying this folder, you will know:|In this folder you learn:|By reading this folder, you should understand:|In this folder, you will learn:|In this folder you will learn:)', '## Learning outcomes', new_text)
            # Replace 'This folder shows/demonstrates/explains/contains/covers' with 'It shows/...'
            def it_replace(m):
                verb = m.group(1)
                return 'It ' + verb

            new_text = re.sub(r'\bThis folder (shows|demonstrates|explains|contains|covers|teaches)\b', it_replace, new_text)
            # Convert remaining 'It shows' phrasing to 'It demonstrates' for consistency
            new_text = re.sub(r'\bIt shows\b', 'It demonstrates', new_text)
            # Normalize alternate learning outcome phrasings to single heading
            new_text = re.sub(r'(?m)^(After studying this folder, you should understand:|After reading this folder, you should understand:|From this folder you will understand:|From this folder, you should learn:|From this folder, you should understand:|From this folder you will understand:)', '## Learning outcomes', new_text)
            # Remove duplicate '## Learning outcomes' occurrences
            new_text = re.sub(r'(## Learning outcomes\n\n)(## Learning outcomes\n)', r'\1', new_text)
            if new_text != text:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_text)
                changed.append(path)

print(f'Updated {len(changed)} README files')
for p in changed:
    print(p)

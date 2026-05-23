import os
import shutil

root = os.path.dirname(__file__)
seen = {}
removed = []
for difficulty in ['easy','medium','hard']:
    dpath = os.path.join(root, difficulty)
    if not os.path.isdir(dpath):
        continue
    for name in sorted(os.listdir(dpath)):
        path = os.path.join(dpath, name)
        if not os.path.isdir(path):
            continue
        if name in seen:
            # remove duplicate
            shutil.rmtree(path)
            removed.append(path)
        else:
            seen[name] = path

print(f'Removed {len(removed)} duplicate folders')
print(f'Unique exercises: {len(seen)}')
for k,v in list(seen.items())[:10]:
    pass
print('Done')

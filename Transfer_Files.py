from os import walk
import shutil

f = []
for (dirpath, dirnames, filenames) in walk('Data'):
    f.extend(filenames)
    print(filenames)
    break

for file in filenames:
    file = f'Data/{file}'
    shutil.copy(file, 'Data/Members')

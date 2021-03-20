from os import walk
import shutil
import json
import sqlite3

con = sqlite3.connect('example.db')

f = []
for (dirpath, dirnames, filenames) in walk('Data/Bills/Congress'):
    f.extend(filenames)
    print(filenames)
    break

for Member in filenames:

    with open(f'Data/Bills/Congress/{Member}', 'r') as g:
        Member_Bills = json.load(g)

    print(Member)

    for Bill in Member_Bills:
        Bill_Type = Bill[0]
        Bill_Name = Bill[1]
        Bill_Link = Bill[2]
        # print([Bill_Type, Bill_Name, Bill_Link])

        with open(f'Data/List_Of_Bills/Name_Link', 'r') as h:
             Bill_List = json.load(h)

        flag = False

        for Bill_Check in Bill_List:
            # print(Bill_Check)

            if Bill_Check == Bill_Name:
                flag = True
                break

        if not flag:
            Bill_List = Bill_List + [[Bill_Type, Bill_Name, Bill_Link]]
            with open(r'Data/List_Of_Bills/Name_Link', 'w') as i:
                json.dump(Bill_List, i, indent=4)

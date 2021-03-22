from os import walk
import shutil
import json
import sqlite3
import time

con = sqlite3.connect('example.db')

c = con.cursor()

# c.execute("""CREATE TABLE Legislation (
#            Leg_Type text,
#            Leg_Name text,
#            Leg_Link text
#            )""")

f = []
for (dirpath, dirnames, filenames) in walk('Data/Bills/Congress'):
    f.extend(filenames)
    # print(filenames)
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

        # print(Bill_Name)

        c.execute("SELECT * FROM Legislation WHERE Leg_Name=:Bill_Name", {'Bill_Name': Bill_Name})

        try:
            fetched_name = c.fetchone()[1]
            #print(f'Duplicate found {Bill_Name} = {fetched_name}')

        except:
            c.execute("INSERT INTO Legislation VALUES(?, ?, ?)", (Bill_Type, Bill_Name, Bill_Link))
            #print(f'Added {Bill_Type}, {Bill_Name}, {Bill_Link}')

        con.commit()

con.close()

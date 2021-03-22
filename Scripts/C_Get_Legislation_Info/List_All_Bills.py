from os import walk
import shutil
import sqlite3
import time

conLeg = sqlite3.connect('../../Data_Bases/Legislation_Only/All.db')
cL = conLeg.cursor()

cL.execute("DROP TABLE Legislation_All")

cL.execute("""CREATE TABLE Legislation_All (
           Type text,
           Name text,
           Link text

           )""")

f = []
for (dirpath, dirnames, filenames) in walk('../../Data_Bases/Congress'):
    f.extend(filenames)
    break

print(filenames)

length = int(len(filenames))

for i in range(length):
    Current_Member = filenames[i][:filenames[i].find('Bills')]
    print(Current_Member)
    # time.sleep(5)

    con2 = sqlite3.connect(f'Data_Bases/Congress/{Current_Member}Bills.db')
    c2 = con2.cursor()

    c2.execute("select *from Congress_Legislation_All ORDER BY Bill_Name;")
    Bills = (c2.fetchall())
    length = int(len(Bills))

    for Bill in Bills:
        Bill_Type = Bill[0]
        Bill_Name = Bill[1]
        Bill_Link = Bill[2]

        # print([Bill_Type, Bill_Name, Bill_Link])

        cL.execute(f"SELECT *FROM Legislation_All WHERE Name=?", (f'{Bill_Name}',))
        Name_Check = cL.fetchone()

        print(str(Bill_Name) + ' ' + str(Name_Check))

        try:
            if str(Bill_Name) == str(Name_Check[1]):
                print(f'duplicate of {Bill_Name} found')
                # time.sleep(5)
                break
        except:
            cL.execute("INSERT INTO Legislation_All VALUES(?, ?, ?)", (Bill_Type, Bill_Name, Bill_Link))
            conLeg.commit()
            print(f'added {Bill_Name}')

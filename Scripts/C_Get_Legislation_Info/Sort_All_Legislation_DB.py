from os import walk
import shutil
import json
import sqlite3
import time
import tkinter as tk

con = sqlite3.connect('example.db')

c = con.cursor()

# Delete Old versions of tables
c.execute("DROP TABLE Legislation_Bills")
# c.execute("DROP TABLE Legislation_Amendments")
# c.execute("DROP TABLE Legislation_Resolutions")
# c.execute("DROP TABLE Legislation_Concurrent_Resolutions")
# c.execute("DROP TABLE Legislation_Joint_Resolutions")
con.commit()

# Get all Bills from Legislation
c.execute("""CREATE TABLE Legislation_Bills (
           Leg_Type text,
           Leg_Name text,
           Leg_Link text
           )""")

c.execute("SELECT * FROM Legislation WHERE Leg_Type='BILL'")
Legislation_Bills = (c.fetchall())
print(Legislation_Bills)

for Bill in Legislation_Bills:

    Bill_Type = Bill[0]
    Bill_Name = Bill[1]
    Bill_Link = Bill[2]

    print(Bill_Name)
    c.execute("INSERT INTO Legislation VALUES(?, ?, ?)", (Bill_Type, Bill_Name, Bill_Link))
    con.commit()

c.execute("select *from Legislation_Bills ORDER BY Leg_Name LIMIT 25;")

Legislation_Bills = (c.fetchall())
for Leg in Legislation_Bills:
    print(Leg)
length = int(len(Legislation_Bills))

window = tk.Tk()

for i in range(length):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"{Legislation[i][j]}")
        label.pack(padx=5, pady=5)

window.mainloop()


# Get all Amendments from Legislation
# c.execute("""CREATE TABLE Legislation_Amendments (
#            Leg_Type text,
#            Leg_Name text,
#            Leg_Link text
#            )""")

# Get all Resolutions from Legislation
# c.execute("""CREATE TABLE Legislation_Resolutions (
#            Leg_Type text,
#            Leg_Name text,
#            Leg_Link text
#            )""")

# Get all Concurrent Resolutions from Legislation
# c.execute("""CREATE TABLE Legislation_Concurrent_Resolutions (
#            Leg_Type text,
#            Leg_Name text,
#            Leg_Link text
#            )""")

# Get all Joint Resolutions from Legislation
# c.execute("""CREATE TABLE Legislation_Joint_Resolutions (
#            Leg_Type text,
#            Leg_Name text,
#            Leg_Link text
#            )""")

print('Done')
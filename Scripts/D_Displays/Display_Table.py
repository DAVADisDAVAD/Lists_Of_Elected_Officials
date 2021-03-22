import requests
from bs4 import BeautifulSoup
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk

con = sqlite3.connect('../../Data_Bases/Congress/Adams, Alma S.Bills.db')

c = con.cursor()

c.execute("select *from Congress_Legislation_All ORDER BY Bill_Name;")
Bills = (c.fetchall())
length = int(len(Bills))

# Test
root = Tk()
root.title('List of Congress Senate')
root.geometry("800x800")

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

for i in range(length):
    for j in range(3):
        Button(second_frame, text=f'{Bills[i][j]}').grid(row=i, column=j, pady=10, padx=10)

root.mainloop()

con.close()







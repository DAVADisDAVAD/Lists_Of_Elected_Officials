import requests
from bs4 import BeautifulSoup
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk

con = sqlite3.connect('../../Data_Bases/Senate_Members.db')

c = con.cursor()

# c.execute("DROP TABLE Senate_Members")
#
# c.execute("""CREATE TABLE Senate_Members (
#            Name text,
#            Party text,
#            District text,
#            link
#
#            )""")
#
# # URL accessed by requests module
# URL = 'https://www.congress.gov/members?q={%22chamber%22:%22Senate%22}&searchResultViewType=expanded'
# page = requests.get(URL)
#
# # HTML parsing
# soup = BeautifulSoup(page.content, 'html.parser')
#
# # Find proper subsection from HTML
# results = soup.find(id='members-senators')
#
# # print(results.prettify())
#
# # turn soup into string
# results = str(results)
#
# # turn string into list
# prelist = results.split('</option>')
#
# # cut wrong results
# prelist = prelist[1:-1]
#
# # step through list of congress man
# for response in prelist:
#     print(response)
#
#     # Get Link to congress.gov page for congressman
#     link = response[response.find('"')+1:response.find('>')-1]
#     print(link)
#
#     # Get name of congressman
#     Name = response[response.find('>')+1:response.find('[')-1]
#     print(Name)
#
#     # Get party affiliation
#     Party = response[response.find('[')+1:response.find('[')+2]
#     print(Party)
#
#     # Get district of congressman
#     District = response[response.find('[')+3:response.find(']')]
#     print(District)
#
#     c.execute("INSERT INTO Senate_Members VALUES(?, ?, ?, ?)", (Name, Party, District, link))
#     # print(f'Added {Bill_Type}, {Bill_Name}, {Bill_Link}')
#
#     con.commit()

c.execute("select *from Senate_Members ORDER BY Name;")
Congress_Members = (c.fetchall())
length = int(len(Congress_Members))

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
    for j in range(4):
        Button(second_frame, text=f'{Congress_Members[i][j]}').grid(row=i, column=j, pady=10, padx=10)

root.mainloop()

con.close()







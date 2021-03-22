import requests
from bs4 import BeautifulSoup
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime

con = sqlite3.connect('../../Data_Bases/Senate_Members.db')
c = con.cursor()

c.execute("select *from Senate_Members ORDER BY Name;")
Senate_Members = (c.fetchall())
length = int(len(Senate_Members))

con.close()

for Senator in Senate_Members:
    SenatorName = Senator[0]
    SenatorName = SenatorName.replace('"', '')
    timestamp = str(datetime.datetime.now())
    print(SenatorName + ' ' + timestamp)

    # Open Connection to senator's DB
    con2 = sqlite3.connect(f'Data_Bases/Senate/{SenatorName}Bills.db')
    c2 = con2.cursor()

    # c2.execute("DROP TABLE SenateMember_Legislation_All")

    c2.execute("""CREATE TABLE Senate_Legislation_All (
               Data text,
               Bill_Name text,
               Link tex

               )""")

    # URL accessed by requests module
    URL = Senator[3]
    # print(URL)
    Bill_List = []

    # Uses request module to get HTML at URL
    page = requests.get(f'{URL}?pageSize=250')

    # HTML parsing
    soup = BeautifulSoup(page.content, 'html.parser')

    # Get last page number from list of bills
    results = soup.find(class_="pagination")
    # print(results.prettify())
    prepage = str(results.find(class_="results-number"))
    # print(prepage)
    Number = prepage[prepage.find('of') + 3:prepage.find('</')]

    try:
        Number = int(Number)
    except:
        Number = 1

    Number = int(Number)
    # print(Number)

    # Start integer when flipping through pages of bills
    i = 1

    # Make thing that flips through pages here
    while i <= Number:

        # URL accessed by requests module set up for flipping through senators congress.gov link and each page of bills
        URL = f'{URL}?pageSize=250&page={i}'
        i = i + 1
        # print(URL)
        page = requests.get(URL)

        # HTML parsing
        soup = BeautifulSoup(page.content, 'html.parser')

        # Find proper subsection from HTML
        results = soup.find(class_="basic-search-results-lists expanded-view")

        bills = results.find_all(class_="expanded")

        for bill in bills:
            # print(bill.prettify())

            # Get if bill or not
            data = str(bill.find(class_="visualIndicator"))
            # print(data)
            data = data[data.find('>') + 1:data.find('</span>')]
            data = data.replace('/n', '')
            data = data.strip()
            # print(data)

            # Get bill number
            PREbillname = bill.find(class_='result-heading')
            PREbillname = str(bill.find('a'))
            billname = PREbillname[PREbillname.find('>') + 1:PREbillname.find('</')]
            billname = billname.replace('/n', '')
            billname = billname.strip()
            # print(billname)

            # Get link to bill
            PRElink = bill.find(class_='result-heading')
            PRElink = str(bill.find('a'))
            # print(PRElink)
            link = "congress.gov" + PRElink[PRElink.find('href="') + 6:PRElink.find('?')]

            c2.execute("INSERT INTO Senate_Legislation_All VALUES(?, ?, ?)", (data, billname, link))
            con2.commit()
    c2.close()




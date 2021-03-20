import requests
from bs4 import BeautifulSoup
import json
import time

# Import Congress_List_Aggregate
with open(f'Data\Members\Congress_List_Aggregate', 'r') as g:
    Congress_List_Aggregate = json.load(g)
    # print(Congress_List_Aggregate)

for Congressman in Congress_List_Aggregate:
    CongressmanName = Congressman[0]
    CongressmanName = CongressmanName.replace('"', '')

    print(CongressmanName)
    # URL accessed by requests module
    URL = Congressman[3]
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

        # URL accessed by requests module set up for flipping through congressmans congress.gov link and each page of bills
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

            Bill_List = Bill_List + [[data, billname, link]]

    print(CongressmanName)
    with open(f'Data\Bills\Congress\\{CongressmanName}', 'w') as f:
        json.dump(Bill_List, f, indent=4)

import requests
from bs4 import BeautifulSoup

EndList = []

# URL accessed by requests module
URL = 'https://www.congress.gov/member/charles-schumer/S000148?pageSize=250'
page = requests.get(URL)

# HTML parsing
soup = BeautifulSoup(page.content, 'html.parser')

# Find proper subsection from HTML
results = soup.find(class_="pagination")

# print(results.prettify())

prepage = str(results.find(class_="results-number"))

print(prepage)

Number = prepage[prepage.find('of') + 3:prepage.find('</')]

Number = int(Number)

print(Number)
Number = 1
i = 1

# Make thing that flips through pages here
while i <= Number:
    i = i + 1
    URLnoPage = 'https://www.congress.gov/member/charles-schumer/S000148?pageSize=250'

    # URL accessed by requests module
    URL = f'{URLnoPage}&page={i}'
    page = requests.get(URL)

    # HTML parsing
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find proper subsection from HTML
    results = soup.find(class_="basic-search-results-lists expanded-view")

    bills = results.find_all(class_="expanded")

    for bill in bills[0:1]:

        print(bill.prettify())

        # Get if bill or not
        data = str(bill.find(class_="visualIndicator"))
        # print(data)
        data = data[data.find('>')+1:data.find('</span>')]
        # print(data)

        # Get bill number
        PREbillname = bill.find(class_='result-heading')
        PREbillname = str(bill.find('a'))
        billname = PREbillname[PREbillname.find('>')+1:PREbillname.find('</')]
        print(billname)

        # Get link to bill
        PRElink = bill.find(class_='result-heading')
        PRElink = str(bill.find('a'))
        # print(PRElink)
        link = "congress.gov" + PRElink[PRElink.find('href="')+6:PRElink.find('">')]
        print(link)

        # Get bill name
        PREbilltitle = bill.find(class_='result-title')
        print(PREbilltitle)
        billtitle = PREbilltitle[PREbilltitle.find('href="') + 6:PREbilltitle.find('">')]


        # Get bill abstract

        # Get bill sponsors


        # Get bill cosponsors (skip till later if difficult)

        # Get commitees

        # Get latest action

        # Get tracker data

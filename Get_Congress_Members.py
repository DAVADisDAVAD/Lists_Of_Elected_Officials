import requests
from bs4 import BeautifulSoup

EndList = []

# URL accessed by requests module
URL = 'https://www.congress.gov/members?q={%22chamber%22:%22Senate%22}&searchResultViewType=expanded'
page = requests.get(URL)

# HTML parsing
soup = BeautifulSoup(page.content, 'html.parser')

# Find proper subsection from HTML
results = soup.find(id='members-representatives')

# print(results.prettify())

# turn soup into string
results = str(results)

# turn string into list
prelist = results.split('</option>')

# cut wrong results
prelist = prelist[1:-1]

# step through list of congress man
for response in prelist:
    print(response)

    # Get Link to congress.gov page for congressman
    link = response[response.find('"')+1:response.find('>')-1]
    print(link)

    # Get name of congressman
    Name = response[response.find('>')+1:response.find('[')-1]
    print(Name)

    # Get party affiliation
    Party = response[response.find('[')+1:response.find('[')+2]
    print(Party)

    # Get district of congressman
    District = response[response.find('[')+3:response.find(']')]
    print(District)

    EndList.append([Name, Party, District, link])

for list in EndList:
    print(list)




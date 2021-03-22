import requests
from bs4 import BeautifulSoup
from Scripts.A_Get_Members import Get_Congress_Members, Get_Senate_Member
import json

List_Congress = Get_Congress_Members.EndList
List_Senate = Get_Senate_Member.EndList
Congress_Aggregate = []
Senate_Aggregate = []

for Member in List_Congress:
    # URL accessed by requests module
    # URL = 'https://www.congress.gov/member/tammy-baldwin/B001230'
    URL = Member[3]
    page = requests.get(URL)

    # HTML parsing
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find proper subsection from HTML
    results = soup.find(class_="standard01 nomargin")

    # print(results.prettify())

    string = str(results)

    # Find website associated with politician
    website = string[string.find('href') + 6:string.find('target') - 2]
    # print(website)

    string = string[string.find('target') - 2:]

    # Find Contact
    address = string[string.find('Contact') + 30: string.find('<br/>')]
    # print(address)
    string = string[string.find('<br/>'):]
    phone = string[string.find('>') + 1:string.find('>') + 15]
    # print(phone)

    # Find Party
    string = string[string.find('"member_party"'):]
    Party = string[string.find('<td>') + 4:string.find('</td>')]
    # print(Party)

    # Find years of Senate membership

    # Find years of house

    print(f'{Member[0]},\n {Party},\n {Member[2]},\n {website},\n {phone},\n {address}')
    # Aggregate Data
    Congress_Aggregate.append([Member[0], Party, Member[2], Member[3], website, phone, address])

with open(f'Data/Congress_List_Aggregate', 'w') as f:
    json.dump(Congress_Aggregate, f, indent=4)

for Member in List_Senate:
    # URL accessed by requests module
    # URL = 'https://www.congress.gov/member/tammy-baldwin/B001230'
    URL = Member[3]
    page = requests.get(URL)

    # HTML parsing
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find proper subsection from HTML
    results = soup.find(class_="standard01 nomargin")

    # print(results.prettify())

    string = str(results)

    # Find website associated with politician
    website = string[string.find('href') + 6:string.find('target') - 2]
    # print(website)

    string = string[string.find('target') - 2:]

    # Find Contact
    address = string[string.find('Contact') + 30: string.find('<br/>')]
    # print(address)
    string = string[string.find('<br/>'):]
    phone = string[string.find('>') + 1:string.find('>') + 15]
    # print(phone)

    # Find Party
    string = string[string.find('"member_party"'):]
    Party = string[string.find('<td>') + 4:string.find('</td>')]
    # print(Party)

    # Find years of Senate membership

    # Find years of house

    print(f'{Member[0]},\n {Party},\n {Member[2]},\n {Member[3]},\n {website},\n {phone},\n {address}')
    # Aggregate Data
    Senate_Aggregate.append([Member[0], Party, Member[2], Member[3], website, phone, address])

with open(f'Data/Senate_List_Aggregate', 'w') as f:
    json.dump(Senate_Aggregate, f, indent=4)


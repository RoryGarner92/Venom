import requests
from bs4 import BeautifulSoup
import re
import csv

business_name = []
street_address = []
address_region = []
postal_code = []
pages = []
rating = []
new = []
nn = []

for i in range(2, 4):
    url = 'https://www.yellowpages.com/search?search_terms=restaurant&geo_location_terms=New%20York%2C%20NY&page=' + str(i)
    pages.append(url)

for p in pages:
    req = requests.get(p)
    soup = BeautifulSoup(req.text, "lxml")
    g_data = soup.find_all("div", {"class": "info"})

    for item in g_data:
        try:
            business_name.append(item.contents[0].find_all("a", {"class": "business-name"})[0].text)
        except:
            pass
        try:
            street_address.append(item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text)
        except:
            pass
        try:
            postal_code.append(item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text)
        except:
            pass
        try:
            rating.append(str(item.contents[1].find_all("div", attrs={"class": "result-rating"})))
        except:
            pass

for word in rating:
    new.append(re.findall(r'"([^"]*)"', word))
for i in new:
     nn.append(i[:1])

rows = zip(business_name, street_address, postal_code, nn)
with open('yellowPages.csv', 'w', encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Business_Name', 'Street_Address', 'Zip_Code', 'rating'])
    for row in rows:
        writer.writerow(row)

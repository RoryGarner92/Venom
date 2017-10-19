#Rory Garner
#C00193506
#IT Carlow
#Software Development

from urllib.request import urlopen
from bs4 import BeautifulSoup

#content = urlopen("http://itcarlow.ie")
content = urlopen("http://testing-ground.scraping.pro/blocks")
soup = BeautifulSoup(content.read(),"lxml")
print(soup.find_all())
#print(content.read())
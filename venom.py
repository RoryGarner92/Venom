from urllib.request import urlopen
from bs4 import BeautifulSoup
import pprint
#content = urlopen("http://itcarlow.ie")
content = urlopen("http://testing-ground.scraping.pro/blocks")
soup = BeautifulSoup(content.read(),"lxml")
print(soup.h1)
#print(content.read())
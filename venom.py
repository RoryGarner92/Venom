#Rory Garner
#C00193506
#IT Carlow
#Software Development

# Currently pulling in all the ratings from the first Yelp search page (link declared below)
# assigning each star rating a variable
# Pulling in the whole review as a list element

from urllib.request import urlopen
from bs4 import BeautifulSoup

#content = urlopen("http://itcarlow.ie")
#content = urlopen("http://testing-ground.scraping.pro/blocks")
#content = urlopen("https://www.yelp.com/biz/new-york-city-new-york-14")
content = urlopen("https://www.yelp.com/search?find_desc=Restaurants&find_loc=New+York,+NY&start=200")

soup = BeautifulSoup(content.read(),"lxml")

div1 = soup.find_all('div', class_="i-stars i-stars--regular-1 rating-large")
div2 = soup.find_all('div', class_="i-stars i-stars--regular-2 rating-large")
div3 = soup.find_all('div', class_="i-stars i-stars--regular-3 rating-large")
div4 = soup.find_all('div', class_="i-stars i-stars--regular-4 rating-large")
div5 = soup.find_all('div', class_="i-stars i-stars--regular-5 rating-large")


fullReview = soup.find_all('li', class_="regular-search-result")
count = len(fullReview)
titleTag = soup.html.head.title


print(fullReview)
print(count)
print(titleTag)
print()
#print(div1,div2,div3,div4, div5)
#print(content.read())
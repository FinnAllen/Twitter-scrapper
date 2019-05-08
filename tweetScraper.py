# @author: Finnian Allen
# Start Date: 5/8/2019
# Description: This project aims to make use of various twitter
# posts by scraping individula tweets and storing them for analysis

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://twitter.com/potus?lang=en').read()

# creates the object "soup" which stores the source and lxml
soup = bs.BeautifulSoup(source, 'lxml')

# gets the title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
#print(soup.p)
#print(soup.get_text())

tweet = soup.find('div', attrs = {'class' : 'js-tweet-text-container'})
print(tweet)

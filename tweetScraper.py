# @author: Finnian Allen
# Start Date: 5/8/2019
# Description: This project aims to make use of various twitter
# posts by scraping individula tweets and storing them for analysis

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://twitter.com/potus?lang=en').read()

# creates the object "soup" which stores the source and lxml
soup = bs.BeautifulSoup(source, 'lxml')

# get twitter user's name:
print(soup.title.string)

# stores the tweet into the "tweet" object
tweet = soup.find('div', attrs = {'class' : 'js-tweet-text-container'})
print(tweet.get_text())

#tweet2 = soup.find_next_sibling(div', attrs = {'class' : 'js-tweet-text-container'})

# @author: Finnian Allen
# Start Date: 5/8/2019
# Description: This project aims to make use of various twitter
# posts by scraping individual tweets and storing them for analysis
# currently runs until ctrl-c, this is so it can update every 30
# seconds

import bs4 as bs
import urllib.request
import time

def scrape():
    # sets the url of the twitter account to scrape
    source = urllib.request.urlopen('https://twitter.com/potus?lang=en').read()
    
    # creates the object "soup" which stores the source and lxml
    soup = bs.BeautifulSoup(source, 'lxml')
    
    # get twitter user's name:
    print(soup.title.string)

    # stores the tweet into the "tweet" object
    tweet = soup.find('div', attrs = {'class' : 'js-tweet-text-container'})
    print(tweet.get_text())

    # call to updater for the recursion
    updater()

    

def updater():
    start_time = time.time()
    
    # loops and scrapes once the condition the time interval has passed
    while(True):
        if(time.time() - start_time > 15):
            scrape()
            


updater()

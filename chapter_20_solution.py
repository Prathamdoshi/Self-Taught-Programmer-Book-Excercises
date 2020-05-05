# chapter 20 solution 

import urllib.request # urlib to get/post content
from bs4 import BeautifulSoup # parsing library


site = "https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en" # source

request_handler = urllib.request.urlopen(site) # make a get call
html = request_handler.read() # read the html from the fetched file
parser = "html.parser" # type of parser

soup = BeautifulSoup(html,parser) # create an instance 

for link in soup.find_all('span',{'class': 'xBbh9'}): # fetches the headlines 
    print(link.contents[0])


#Print out article text of website
#http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
#Use BeautifulSoup and requests python packages

import requests
url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(r_html, 'html.parser')

paragraph = soup.find_all('p')

for i in paragraph[4:]:
    title = i.text
    print(title)


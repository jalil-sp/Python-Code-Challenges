#Print out list of article titles on NYTimes homepage
#Use BeautifulSoup and requests python packages

import requests
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

from bs4 import BeautifulSoup

#print(r_html)

'''
<h3 class="indicate-hover css-1gb49m4">The Presidential Candidate Who Has His Own Supporters Scratching Their Heads</h3>
'''
soup = BeautifulSoup(r_html, 'html.parser')

#links = soup.find_all('h3')
links = soup.find_all(class_= 'indicate-hover')
print(links)

for tag in links:
    title = tag.text
    print(title)
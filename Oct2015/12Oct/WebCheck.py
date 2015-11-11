__Date__ = '11/10/2015'
"""
From "http://www.practicepython.org/"*****************
16)Use the BeautifulSoup and requests Python packages to print out a list of all
the article titles on the New York Times homepage.
http://www.nytimes.com/
"""
from bs4 import BeautifulSoup as bfs
import requests
nyurl='http://www.nytimes.com/'
html = requests.get(nyurl)
soup=bfs(html.text,"html.parser")
for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())

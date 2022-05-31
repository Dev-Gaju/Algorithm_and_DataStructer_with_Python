# import lxml
from bs4 import BeautifulSoup
import requests

with open('home.html', 'r') as home_file :
    content = home_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'html.parser')
    # print(soup)
    # tags = soup.find('h2')
    tags = soup.find_all('h2')
    print(tags)
    for element in tags:
        print(element.text)
    div_classes = soup.find_all('div', class_ = 'card')   # div class extra properties
    for course in div_classes:
        course_name = course.h5.text
        course_price = course.a

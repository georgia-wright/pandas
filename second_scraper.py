from bs4 import BeautifulSoup

import requests

import pandas as pd

import numpy as np

with open ('index.html', 'r') as file:
    html_text = file.read()

souped_html = BeautifulSoup(html_text, "lxml")

topics = [

]

column_1 = souped_html.find_all('h3')

for topic in column_1:
    topics.append(topic.text.strip())


first = [

]

column_2 = souped_html.find_all(class_= "first")

for item in column_2:
    first.append(item.text.strip())


second = [

]

column_3 = souped_html.find_all(class_= "second")

for item in column_3:
    second.append(item.text.strip())


third = [


]


column_4 = souped_html.find_all(class_= "third")

for item in column_4:
    third.append(item.text.strip())

# print(third)


df = pd.DataFrame ({
    "Topic" : topics,
    "First" : first,
    "Second" : second,
    "Third" : third
})

print(df)


df.to_excel("my_website.xlsx") 







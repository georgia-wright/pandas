from bs4 import BeautifulSoup

import requests

import pandas as pd

import numpy as np

html_text = requests.get("https://www.scrapethissite.com/pages/simple/").text

# print(html_text)

# print(html_text)

souped_html = BeautifulSoup(html_text, "lxml")

countries_list = [


]

countries = souped_html.find_all('h3')

for country in countries:
    countries_list.append(country.text.strip())


# df = pd.DataFrame([country.text.strip() for country in countries])

# print(df)
    

capitals = [


]

country_capitals = souped_html.find_all('span', class_ = "country-capital")

for capital in country_capitals:
    capitals.append(capital.text.strip())

populations = [



]

country_populations = souped_html.find_all('span', class_ = "country-population")

for population in country_populations:
    populations.append(population.text.strip())



areas = [

]


country_area = souped_html.find_all('span', class_ = "country-area")

for area in country_area:
    areas.append(area.text.strip())




df = pd.DataFrame ({
    "Countries" : countries_list,
    "Capitals" : capitals,
    "Population" : populations,
    "Area" : areas
})
    
print(df)


df.to_excel("output.xlsx") 








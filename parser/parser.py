import json

import requests
from bs4 import BeautifulSoup
"""
Work in progress
"""


class Flat:
    def __init__(self, link, price_rub, price_d, price_e):
        self.link = link
        self.price_rub = price_rub
        self.price_d = price_d
        self.price_e = price_e


response = requests.get(
    "https://www.avito.ru/nizhniy_novgorod/kvartiry/prodam?s=101")

bs = BeautifulSoup(response.text, "html.parser")

flats = []
for i in bs.find_all(class_="item"):
    d = json.loads(i.find('div', class_="popup-prices")['data-prices'])
    link = i.find('a', class_="item-description-title-link")['href']

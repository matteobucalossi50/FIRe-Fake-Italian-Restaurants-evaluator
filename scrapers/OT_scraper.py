from bs4 import BeautifulSoup
import requests
import re
import json
import urllib.request as urllib2
import pandas as pd
from os import listdir
from os.path import isfile, join

# creating a function that converts a list to a string
def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))

def get_menus(url):
    myfile = requests.get(url)
    soup = BeautifulSoup(myfile.content, 'lxml')
    dishes = soup.select('p[class^="menu"]')

    dishes_cleaned = []

    for dish in dishes:
        dish = str(dish)
        dish = dish.replace('<p class="menu-description__2HXkC4oE">', "")
        dish = dish.replace('</p>', "")
        dish = dish.replace('<p class="menu-section-description__1NOsGasf">', "")
        dishes_cleaned.append(dish)

    dishes_cleaned = [' '.join(i for i in dishes_cleaned)]

    dishes_cleaned = listToString(dishes_cleaned)

    dishes_cleaned = re.sub('[^a-zA-ZÀ-ÿ.\s]', '', dishes_cleaned)
    dishes_cleaned = dishes_cleaned.lower()

    return dishes_cleaned

def corpus_builder(text):
    OpenTable_Corpus = []

    for menu in text:
        OpenTable_Corpus.append(get_menus(menu))
    return OpenTable_Corpus

menus = ["https://www.opentable.com/r/crudite-milano-milan", "https://www.opentable.com/r/risotteria-italiana-milan?corrid=9cf72e53-c4ec-4acf-ba3a-6cf9a9ae8daa&p=2&sd=2020-03-31%2022%3A30",
        "https://www.opentable.com/r/terrazza-241-como?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=eb46a391-a86e-47d7-9fd3-8e432db6fbf2&p=2&sd=2020-04-30%2023%3A00",
        "https://www.opentable.com/r/satin-como?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=eb46a391-a86e-47d7-9fd3-8e432db6fbf2&p=2&sd=2020-04-30%2023%3A00",
        "https://www.opentable.com/r/savo-gourmet-pizzeria-genova?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=5d8db339-e2c5-48db-bebe-cdcae29f3754&p=2&sd=2020-04-30+23%3A00",
        "https://www.opentable.it/r/ristorante-tenuta-fasano-naples?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=55bed57d-8db4-4580-87f3-cb1b43638fc8&p=2&sd=2020-05-10%2019%3A00",
        "https://www.opentable.it/r/le-isole-marsala?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=55bed57d-8db4-4580-87f3-cb1b43638fc8&p=2&sd=2020-05-10%2019%3A00",
        "https://www.opentable.it/r/libra-cucina-evolution-bologna?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=d401c110-7094-45fc-82cf-843bbb04d13a&p=2&sd=2020-05-10+19%3A00",
        "https://www.opentable.it/r/terrazza-danieli-venice?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=8d103dfc-4f8d-4066-b5e4-2231f10d6b42&p=2&sd=2020-05-22+19%3A00",
        "https://www.opentable.it/r/giardino-dinverno-venice?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=8d103dfc-4f8d-4066-b5e4-2231f10d6b42&p=2&sd=2020-05-22+19%3A00",
        "https://www.opentable.it/r/savo-gourmet-pizzeria-genova?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=269cccf0-9ccb-48e0-a2d1-44c91ec8ad2f&p=2&sd=2020-05-22+19%3A00",
        "https://www.opentable.it/r/mi-garba-milan?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=c706d767-bac1-4a00-bea7-ac4856784522&p=2&sd=2020-05-22%2019%3A00",
        "https://www.opentable.it/r/ristorante-alle-langhe-milan?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=c706d767-bac1-4a00-bea7-ac4856784522&p=2&sd=2020-05-22%2019%3A00",
        "https://www.opentable.it/r/god-save-the-food-piave-milan?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=c706d767-bac1-4a00-bea7-ac4856784522&p=2&sd=2020-05-22%2019%3A00",
        "https://www.opentable.it/r/osteria-della-via-appia-milano?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=c706d767-bac1-4a00-bea7-ac4856784522&p=2&sd=2020-05-22%2019%3A00",
        "https://www.opentable.it/r/la-pizza-biscottata-gourmet-milan?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=c706d767-bac1-4a00-bea7-ac4856784522&p=2&sd=2020-05-22%2019%3A00",
        "https://www.opentable.it/r/caffe-and-bistrot-la-locanda-del-gatto-rosso-milan?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=c706d767-bac1-4a00-bea7-ac4856784522&p=2&sd=2020-05-22+19%3A00",
        "https://www.opentable.it/r/risotteria-italiana-milan?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=c706d767-bac1-4a00-bea7-ac4856784522&p=2&sd=2020-05-22%2019%3A00",
        ]

corpus_builder(menus)
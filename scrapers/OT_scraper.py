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


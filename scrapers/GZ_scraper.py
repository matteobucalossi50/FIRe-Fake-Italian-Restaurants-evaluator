from bs4 import BeautifulSoup
import re
import json
import urllib.request as urllib2

# creating a function that converts a list to a string
def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


def get_ingredients(url):
    # retrieving the url in json format
    myurl = urllib2.urlopen(url).read()
    soup = BeautifulSoup(myurl)
    ingredients = json.loads(soup.find('script', type='application/ld+json').text)

    # cleaning the text:
    ingredients = str(ingredients)
    ingredients = ingredients.split('[')  # splitting the text by [
    ingredients = ingredients[1:3]  # getting the ingredients and cooking instructions
    ingredients = [i.split(']', 1)[0] for i in ingredients]  # splitting the text by ] and consolidating the text

    ingredients = listToString(ingredients)  # converting the text to a string

    ingredients = re.sub('[^a-zA-ZÀ-ÿ.\s]', '', ingredients)  # removing all the numbers and special characters

    ingredients = ingredients.lower()  # lowering the case

    return ingredients

#Consolidating all the recipes in a list
def corpus_builder(text):
    GialloZafferano_Corpus = []

    for recipe in text:
        GialloZafferano_Corpus.append(get_ingredients(recipe))
    return GialloZafferano_Corpus


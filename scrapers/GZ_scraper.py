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


# import recipes
recipes = ["https://ricette.giallozafferano.it/Spaghetti-alla-Carbonara.html", "https://ricette.giallozafferano.it/Spaghetti-all-Amatriciana.html",
           "https://ricette.giallozafferano.it/Risotto-allo-Zafferano.html", "https://ricette.giallozafferano.it/Spezzatino-di-manzo.html",
          "https://ricette.giallozafferano.it/Tiramisu.html", "https://ricette.giallozafferano.it/Pasta-al-forno.html",
          "https://ricette.giallozafferano.it/Paccheri-ripieni-con-salsiccia-e-funghi.html", "https://ricette.giallozafferano.it/Spaghetti-allo-scoglio.html",
          "https://ricette.giallozafferano.it/Pasta-gorgonzola-e-noci.html", "https://ricette.giallozafferano.it/Parmigiana-di-melanzane.html",
          "https://ricette.giallozafferano.it/Polpettine-di-tonno-e-ricotta.html", "https://ricette.giallozafferano.it/Filetto-al-pepe-verde.html",
          "https://ricette.giallozafferano.it/Zucchine-ripiene.html", "https://ricette.giallozafferano.it/Saltimbocca-alla-Romana.html",
          "https://ricette.giallozafferano.it/Rotolo-di-frittata-farcito.html", "https://ricette.giallozafferano.it/Scaloppine-ai-funghi.html",
          "https://ricette.giallozafferano.it/Tiramisu.html", "https://ricette.giallozafferano.it/Tortino-di-cioccolato-con-cuore-fondente.html",
          "https://ricette.giallozafferano.it/Crema-pasticcera.html", "https://ricette.giallozafferano.it/Torta-rustica-di-mele.html",
          "https://ricette.giallozafferano.it/Crostata-alla-frutta.html", "https://ricette.giallozafferano.it/Crostata-morbida-al-cioccolato.html",
          "https://ricette.giallozafferano.it/Cannoli-siciliani.html", "https://ricette.giallozafferano.it/Torta-margherita.html",
          "https://ricette.giallozafferano.it/Bigne-alla-crema.html", "https://ricette.giallozafferano.it/Taralli.html",
          "https://ricette.giallozafferano.it/Arancini-di-riso.html", "https://ricette.giallozafferano.it/Mozzarella-in-carrozza.html",
          "https://ricette.giallozafferano.it/Focaccia-con-pomodorini-e-origano.html", "https://ricette.giallozafferano.it/Grissini.html",
          "https://ricette.giallozafferano.it/Frittata-di-zucchine.html", "https://ricette.giallozafferano.it/Involtini-di-melanzane.html",
          "https://ricette.giallozafferano.it/Insalata-di-polpo-prezzemolata.html", "https://ricette.giallozafferano.it/Asparagi-in-sfoglia-con-crudo.html",
          "https://ricette.giallozafferano.it/Carciofi-ripieni.html", "https://ricette.giallozafferano.it/Patate-al-forno.html",
          "https://ricette.giallozafferano.it/Sformato-di-verdure.html", "https://ricette.giallozafferano.it/Verdure-gratinate-al-forno.html",
          "https://ricette.giallozafferano.it/Peperonata.html", "https://ricette.giallozafferano.it/Cipolline-in-agrodolce.html",
          "https://ricette.giallozafferano.it/Polpettone-alla-ligure.html", "https://ricette.giallozafferano.it/Insalata-di-ceci-gamberi-e-rucola.html",
          "https://ricette.giallozafferano.it/Insalata-con-avocado.html", "https://ricette.giallozafferano.it/Fagiolini-alla-pugliese.html",
          "https://ricette.giallozafferano.it/Panzerotti-calzoni-fritti.html", "https://ricette.giallozafferano.it/Treccia-di-pasta-lievitata.html",
          "https://ricette.giallozafferano.it/Pizza-Margherita.html", "https://ricette.giallozafferano.it/Focaccia-col-formaggio.html",
          "https://ricette.giallozafferano.it/Pane-ai-cereali.html", "https://ricette.giallozafferano.it/Risotto-alla-salsiccia.html",
          "https://ricette.giallozafferano.it/Risotto-ai-funghi.html", "https://ricette.giallozafferano.it/Risotto-radicchio-e-pancetta.html"]

corpus_builder(recipes)
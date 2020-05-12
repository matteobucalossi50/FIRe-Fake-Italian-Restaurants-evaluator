import pandas as pd
import simplejson as json
from analysis.simple_spell import *
from scrapers.TestCorpusScraper_editing import *
from analysis.scoring import *
import warnings
warnings.filterwarnings('ignore')




#!pip install nltk

#Importing the background corpus
with open('data/Background Corpora.json', 'r') as j:
        Background_Corpora_Json = json.load(j)

words_freq = tf(Background_Corpora_Json)


#Test File
food_words = cooking_corpus_creator("https://www.enchantedlearning.com/wordlist/food.shtml") 
food_verbs = cooking_corpus_creator("https://www.enchantedlearning.com/wordlist/cooking.shtml") 
cooking_vocabulary = food_words + food_verbs
cooking_vocabulary




#test = pd.read_csv('./scrapers/Filomena.csv')

url = input("Enter the url to be tested")


test_menu = get_menusII(url)

test_menu = remove_english(str(test_menu), cooking_vocabulary)



menu = set_menu(test_menu)

result, errs = checker(words_freq.keys(), menu)

print("These are the errors:", errs)
print("Result:",result)

scores = scoring(result, 1)


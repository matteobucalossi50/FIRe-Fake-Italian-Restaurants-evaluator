import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import simplejson as json
from analysis.simple_spell import *
from scrapers.TestCorpusScraper_editing import *
from analysis.scoring import *
import warnings
warnings.filterwarnings('ignore')


# Importing the background corpus
with open('data/Background Corpora.json', 'r') as j:
        Background_Corpora_Json = json.load(j)

# Get tokens dictionary
words_freq = tf(Background_Corpora_Json)

# english words to exclude
food_words = cooking_corpus_creator("https://www.enchantedlearning.com/wordlist/food.shtml") 
food_verbs = cooking_corpus_creator("https://www.enchantedlearning.com/wordlist/cooking.shtml") 
cooking_vocabulary = food_words + food_verbs

###test = pd.read_csv('./scrapers/Filomena.csv')


# user menu
url = input("Enter the url to be tested: ")

test_menu = get_menusII(url)
test_menu = remove_english(str(test_menu), cooking_vocabulary)
menu = set_menu_user(test_menu)

# check the menu
result, errs = checker(words_freq.keys(), menu)
print("These are the errors:", errs)
print("Detected errors:", result)

# get our score!
score, img, image = scoring(result)

plt.imshow(img)
plt.show()
input("Got it now? (Press any key): ")
plt.close()

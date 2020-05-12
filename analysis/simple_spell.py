import json
from nltk.metrics import *
from analysis.Indexes import *

# import test menu
def menu_test(test_json):
    with open(test_json, 'r') as j:
        Test_menu = json.load(j)
    return Test_menu
    
# import background corpus
def background_corpus():
    with open('./data/Background Corpora.json', 'r') as j:
        Background_Corpora_Json = json.load(j)


#words_freq = tf(Background_Corpora_Json)

def set_menu(Test_menu):
    set_menu = set(get_tokens_stopw(Test_menu))
    # print(set_menu)
    # print(len(set_menu))
    return set_menu


def checker(background, test):
    count = 0
    errors = []
    for element in test:
        if element not in set(background):
            errors.append(element)
            count += 1
        else:
            continue
    return count, errors

#result, errs = checker(words_freq.keys(), set_menu)





# edit_distance
'''
target_word = "fire"
possible_misspellings = [word for sentence in error_newswire for word in sentence if edit_distance(word, target_word) < 2 and edit_distance(word, target_word) > 0]
print(possible_misspellings)
'''

#def edit(test_menu, words_freq.keys()):
 #   count = 0
  #  for word in test_menu:
   #     for w in words_freq.keys():
    #        if edit_distance(word, w) < 2 and edit_distance(word, w) > 0:
     #           print(word)
      #          count += 1
    # return count
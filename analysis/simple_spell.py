import json
from nltk.metrics import *
from scrapers import indexes

# import test menu
with open('Ristorante Angolo.json', 'r') as j:
    Test_menu = json.load(j)
    print(Test_menu)
# import background corpus
with open('Background Corpora.json', 'r') as j:
    Background_Corpora_Json = json.load(j)
    print(Background_Corpora_Json)

words_freq = indexes.tf(Background_Corpora_Json)

set_menu = set(indexes.get_tokens_stopw(Test_menu))
print(set_menu)
len(set_menu)


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

result, errs = checker(words_freq.keys(), set_menu)





# edit_distance
'''
target_word = "fire"
possible_misspellings = [word for sentence in error_newswire for word in sentence if edit_distance(word, target_word) < 2 and edit_distance(word, target_word) > 0]
print(possible_misspellings)
'''
count = 0
for word in test_menu:
    for w in words_freq.keys():
        if edit_distance(word, w) < 2 and edit_distance(word, w) > 0:
            print(word)
            count += 1
print(count)
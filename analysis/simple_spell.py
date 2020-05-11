import json
from nltk.metrics import *
from scrapers import indexes

# import test menu
with open('Test Corpus.json', 'r') as j:
    Test_Corpus = json.load(j)
    print(Test_Corpus)
# import background corpus
with open('data/Background Corpora.json', 'r') as j:
    Background_Corpora_Json = json.load(j)
    print(Background_Corpora_Json)

words_freq = indexes.tf(Background_Corpora_Json)

# get tokens of each menu
tokens_test_sw = {}
for key, value in Test_Corpus.items():
    all_tokens_t = []
    for item in value:
        punkt_sentences = sentence_tokenizer.tokenize(item)
        sentences_words = [treebank_tokenizer.tokenize(sentence) for sentence in punkt_sentences]
        all_tokens = [word for sentence in sentences_words for word in sentence]
        all_tokens = [word.lower() for word in all_tokens if word.isalpha()]
        all_tokens = [word for word in all_tokens if word != 'g']

        stop_words = nltk.corpus.stopwords.words('italian')
        all_tokens = [w for w in all_tokens if w not in stop_words]

        for w in all_tokens:
            all_tokens_t.append(w)

    tokens_test_sw[key] = all_tokens_t

# make each menu a set
set_tokens_test_sw = {}
for key, value in tokens_test_sw.items():
    set_menu = set(value)
    set_tokens_test_sw[key] = set_menu

print(set_tokens_test_sw)
len(set_tokens_test_sw)


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


# finally check them
final_results = {}
final_errors = {}
for key, value in set_tokens_test_sw.items():
    result, errs = checker(words_freq.keys(), value)
    final_results[key] = result
    final_errors[key] = errs




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
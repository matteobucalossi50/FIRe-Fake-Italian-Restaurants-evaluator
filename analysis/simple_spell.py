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
    return Background_Corpora_Json


#words_freq = tf(Background_Corpora_Json)

# get tokens of each menu
def get_tokens_test(corpus):
    tokens_test_sw = {}
    for key, value in corpus.items():
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

    return tokens_test_sw


# make each menu a set
def set_menu(dict):
    set_tokens_test_sw = {}
    for key, value in dict.items():
        set_menu = set(value)
        set_tokens_test_sw[key] = set_menu
    return set_tokens_test_sw


# checker function
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
# final_results = {}
# final_errors = {}
# for key, value in set_tokens_test_sw.items():
#     result, errs = checker(words_freq.keys(), value)
#     final_results[key] = result
#     final_errors[key] = errs


#result, errs = checker(words_freq.keys(), set_menu)





# edit_distance

def edit_dist(dic, corr_w):
    count = 0
    misspells = []
    for key, value in dic.items():
        for word in value:
            if edit_distance(word, corr_w) < 2 and edit_distance(word, corr_w) > 0:
                misspells.append(word)
                count += 1
    return misspells, count

# v expensive?
# missp_dic = {}
# for w in words_freq.keys():
#     misspells, count = edit_dist(tokens_test_s, w)
#     missp_dic[w] = misspells


# try with jaro distance
def jaro_dist(dic, corr_w):
    count = 0
    misspells = []
    for key, value in dic.items():
        for word in value:
            if jaro_similarity(word, corr_w) < 2 and jaro_similarity(word, corr_w) > 0:
                misspells.append(word)
                count += 1
    return misspells, count

# # v expensive?
# missp_dic = {}
# for w in words_freq.keys():
#     misspells, count = jaro_dist(tokens_test_s, w)
#     missp_dic[w] = misspells


from nltk.metrics import *




# edit distance
def edit_dist(dic, corr_w):
    count = 0
    misspells = []
    for key, value in dic.items():
        for word in value:
            if edit_distance(word, corr_w) < 2 and edit_distance(word, corr_w) > 0:
                if word not in misspells:
                    misspells.append(word)
                    count += 1
    return misspells, count

# v expensive?
def get_candidates(dic, words_freq):
    missp_dic = {}
    for w in words_freq.keys():
        misspells, count = edit_dist(dic, w)
        if count != 0:
            missp_dic[w] = misspells


# try with jaro distance
# def jaro_dist(dic, corr_w):
#     count = 0
#     misspells = []
#     for key, value in dic.items():
#         for word in value:
#             if jaro_similarity(word, corr_w) < 2 and jaro_similarity(word, corr_w) > 0:
#                 misspells.append(word)
#                 count += 1
#     return misspells, count
#
# # # v expensive?
# missp_dic = {}
# for w in words_freq.keys():
#     misspells, count = jaro_dist(tokens_test_s, w)
#     missp_dic[w] = misspells


# grams frequencies
freq_bi = nltk.FreqDist(bigrams)

print(freq_bi.most_common(20))
freq_bi.plot(10)


'''
print(freq_bi.N())
print(freq_bi.freq(('pizza', 'napoletana')))
'''


#MLE_Dist = nltk.MLEProbDist(freq_bi)
Smoothed_dist = nltk.LaplaceProbDist(freq_bi)

print(Smoothed_dist.prob(('Chair', 'Force')))
print(Smoothed_dist.logprob(('Chair', 'Force')) )

'''
def get_better_sentence_bigrams(sentence):
    sentence_words = treebank_tokenizer.tokenize(sentence)
    stop_words = nltk.corpus.stopwords.words('english')
    content = [w for w in sentence_words if w.lower() not in stop_words]
    word_count = len(sentence_words)
    bigrams = nltk.bigrams(content)
    return bigrams, word_count
    '''


def estimate_sentence_probability(ngrams, word_count):
    slogprob = 0
    for bigram_words in ngrams:
        logprob = Smoothed_dist.logprob(bigram_words)
        slogprob += logprob

    return slogprob / word_count

estimate_probability = estimate_sentence_probability(all_ngrams, word_count)
print(estimate_probability)



# generate plots of tf, grams, terms-docs


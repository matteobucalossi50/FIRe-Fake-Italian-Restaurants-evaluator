import spacy
nlp = spacy.load("it_core_news_sm")
import nltk.data
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import word_tokenize
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
treebank_tokenizer = TreebankWordTokenizer()
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
from nltk.stem.porter import *
porter_stemmer = PorterStemmer()
from nltk import ngrams

with open('Background Corpora.json', 'r') as j:
    Background_Corpora_Json = json.load(j)
    print(Background_Corpora_Json)

def get_tokens(text):
    punkt_sentences = sentence_tokenizer.tokenize(text)
    sentences_words = [treebank_tokenizer.tokenize(sentence) for sentence in punkt_sentences]
    all_tokens = [word for sentence in sentences_words for word in sentence]
    all_tokens = [word.lower() for word in all_tokens if word.isalpha()]
    all_tokens = [word for word in all_tokens if word != 'g']

    #     stop_words = nltk.corpus.stopwords.words('italian')
    #     all_tokens = [w for w in all_tokens if w not in stop_words]
    return all_tokens


def get_tokens_stopw(text):
    punkt_sentences = sentence_tokenizer.tokenize(text)
    sentences_words = [treebank_tokenizer.tokenize(sentence) for sentence in punkt_sentences]
    all_tokens = [word for sentence in sentences_words for word in sentence]
    all_tokens = [word.lower() for word in all_tokens if word.isalpha()]
    all_tokens = [word for word in all_tokens if word != 'g']

    stop_words = nltk.corpus.stopwords.words('italian')
    all_tokens = [w for w in all_tokens if w not in stop_words]
    return all_tokens


def trigram(sentence):
    # create a list for the result
    result = list()
#     # create a list that contains no punctuation
#     sentence = list()
#     # parse through the document to add all tokens that are words to the sentence list
#     for token in doc:
#         if token.is_alpha:
#             sentence.append(token)
    # parse through the sentence while adding words in groups of two to the result
    for word in range(len(sentence) - 2):
        first_word = sentence[word]
        second_word = sentence[word + 1]
        third_word = sentence[word + 2]
        element = [first_word, second_word, third_word]
        result.append(element)

    return result


def bigram_spacy(corpus, nlp):
    # trying with spacy by sentence
    res = []
    for key, value in corpus.items():
        # print(doc)
        doc = nlp(value)

        for sent in doc.sents:
            res.append(trigram(sent))
    return res


def ngrams_it(corpus):
    all_ngrams = []
    # get all ngrams
    for key, value in corpus.items():
        # print(doc)
        tokens = get_tokens(value)
        res = trigram(tokens)
        # res = ngrams(tokens, 2)
        for gram in res:
            all_ngrams.append(gram)

    return all_ngrams


def tf(corpus):
    words_freq = {}
    for key, value in corpus.items():
        tokens = get_tokens_stopw(value)
        for token in tokens:
            if token not in words_freq.keys():
                words_freq[token] = 1
            else:
                words_freq[token] += 1

    # words_freq = sorted(words_freq.items(), key=lambda x:x[1], reverse=True)
    return words_freq

def tf_doc(corpus):
    doc_terms = {}
    for key, value in corpus.items():
        term_freq = {}
        tokens = get_tokens_stopw(value)
        for token in tokens:
            if token not in term_freq.keys():
                term_freq[token] = 1
            else:
                term_freq[token] += 1
        doc_terms[key] = term_freq

    return doc_terms

def get_alltokens(corpus):
    all_tokens = []

    for key, value in corpus.items():
        tokens = get_tokens_stopw(value)
        for tok in tokens:
            if tok not in all_tokens:
                all_tokens.append(tok)
            else:
                continue
    return all_tokens


def inv_index(corpus, all_tokens):
    term_docs = {}
    for tok in all_tokens:
        doc_dic = {}
        documents = []
        for key, value in corpus.items():
            tokens = get_tokens_stopw(value)
            if tok in tokens:
                documents.append(key)
            else:
                continue
        term_docs[tok] = documents

    return term_docs


def term_grams(all_tokens, all_ngrams):
    grams_dic = {}

    for tok in all_tokens:
        grams = []
        for gram in all_ngrams:
            if tok in gram:
                grams.append(gram)

        grams_dic[tok] = grams

    return grams_dic


def term_doc_grams(all_tokens, corpus, all_ngrams):  # n^3 v slow
    dic = {}
    for tok in all_tokens:
        doc_dic = {}
        for key, value in corpus.items():
            grams = []
            for gram in all_ngrams:
                if tok in gram:
                    grams.append(gram)
            doc_dic[key] = grams
        dic[tok] = doc_dic
    return dic



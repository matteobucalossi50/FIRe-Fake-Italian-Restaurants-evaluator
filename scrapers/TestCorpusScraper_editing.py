#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import nltk
#nltk.dowload('words')
from nltk.corpus import words
from nltk.tokenize import TreebankWordTokenizer
treebank_tokenizer = TreebankWordTokenizer()
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from nltk.stem import RegexpStemmer
import re


# In[ ]:


#creating a function that converts a list to a string
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s))


# In[ ]:


def get_menusII(url):
    myfile = requests.get(url)
    soup = BeautifulSoup(myfile.content)
    
    menu = soup.findAll("div", {"class": "menu-item-header__3xwnFL-n"})
    #descriptions = soup.findAll("p", {"class": "menu-description__2HXkC4oE"})
    #menu = headers + descriptions
    
    for w in range(0, len(menu)):   
        menu[w] = str(menu[w])                     #converting the objects to strings
        menu[w] = re.sub('<[^>]+>', '', menu[w])   #eliminaiting the scripts in between <>
        
    menu = [' '.join(w for w in menu)] 
    
    menu = listToString(menu)
    menu = menu.lower() #lowercasing every word
    
    menu = re.sub('[^a-zA-ZÀ-ÿ.\s]', '', menu) #removing all the numbers and special characters
    menu = menu.replace(".", "")

    return menu



# In[ ]:


#test1


# In[ ]:


def cooking_corpus_creator(url):
    myfile = requests.get(url)
    soup = BeautifulSoup(myfile.content)
    
    cooking_words = soup.findAll("div", {"class": "wordlist-item"})
    
    for w in range(0, len(cooking_words)):   
        cooking_words[w] = str(cooking_words[w])                     #converting the objects to strings
        cooking_words[w] = re.sub('<[^>]+>', '', cooking_words[w])
    
    return cooking_words

#cooking_corpus_creator("https://www.enchantedlearning.com/wordlist/cooking.shtml")   


# In[ ]:


#food_words = cooking_corpus_creator("https://www.enchantedlearning.com/wordlist/food.shtml") 
#food_verbs = cooking_corpus_creator("https://www.enchantedlearning.com/wordlist/cooking.shtml") 
#cooking_vocabulary = food_words + food_verbs
#cooking_vocabulary


# In[ ]:





# In[ ]:


def remove_english(text, cooking_list):
    stemmer = RegexpStemmer("ed$|'s$")
    stemmer1 = RegexpStemmer("d$")
    text = treebank_tokenizer.tokenize(text)
    lemmatized_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    lemmatized_text = [w for w in lemmatized_text if w not in cooking_list]
    
    lemmatized_stemmed_text = []

    for w in lemmatized_text:
        w = stemmer.stem(w)
        w = stemmer1.stem(w)
        lemmatized_stemmed_text.append(w)
        
    tokenized_Italian_text = [w for w in lemmatized_stemmed_text if w not in words.words()]
    Italian_text = ' '.join(tokenized_Italian_text)
    
    Italian_text = re.sub('[^a-zA-ZÀ-ÿ.\s]', '', Italian_text) #removing all the numbers and special characters
    
    return Italian_text

#remove_english(test1)


# In[ ]:


#"mushroom" in words.words()


# In[ ]:


#def remove_english(text):
    
 #   text = treebank_tokenizer.tokenize(text)
  #  lemmatized_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
   # lemmatized_text = [w for w in lemmatized_text if w not in cooking_vocabulary]

    
    #lemmatized_stemmed_text = []

    #for w in lemmatized_text:
     #   w = stemmer.stem(w)
      #  w = stemmer1.stem(w)
       # lemmatized_stemmed_text.append(w)
        
    #tokenized_Italian_text = [w for w in lemmatized_stemmed_text if w not in words.words()]
    #tokenized_Italian_text = [w for w in tokenized_Italian_text if w not in cooking_vocabulary]
    #Italian_text = ' '.join(tokenized_Italian_text)
    
    #Italian_text = re.sub('[^a-zA-ZÀ-ÿ.\s]', '', Italian_text) #removing all the numbers and special characters
    
    #return Italian_text



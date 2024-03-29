# CS390Z - Introduction to Data Minining - Fall 2021
# Instructor: Thyago Mota
# Description: Activity 22: Illustrates NLKT

import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import 	WordNetLemmatizer
from nltk import ne_chunk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import requests 
import os

# definitions/parameters
GUTENBERG_URL = "https://www.gutenberg.org/files/1342/1342-0.txt"
DATA_FOLDER = "../data"
OUTPUT_FILE = "word_tokens.txt"

if __name__ == "__main__":

    # TODO: obtain the raw text as a string

    # TODO: extract word tokens from raw text

    # TODO: extract sentence tokens from raw text

    # TODO: count how many time the word "love" appears

    # TODO: save all tokens in a text file (one word token per line)
    
    # TODO: POS taggging

    # TODO: show only nouns

    # TODO: for each of the nouns, show its stem and lemma

    # TODO: perform a NER tagging

    # TODO: compute a bag of words for each sentence, create a dictionary associating a word and its frequency, sort it by frequency (descending order)

    # TODO: do the same but for bigrams
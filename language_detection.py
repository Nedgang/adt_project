#!/usr/bin/env python3

# -*- coding: utf8 -*-

import sys
import nltk
try:
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print("You need to install the corpora (~2.4Go): nltk.download()")

from nltk.tokenize import wordpunct_tokenize


def get_language_nltk(tokens):
    """
        Extract the language from an array of tokens, it is based on stop words
        and use the nltk corpora as reference

        If you don't have the corpora you can install them by nltk.download()
        and using the id "all", it may take some time to downlaod and ~ 2.4Go

        improvement: if 2 language have equal score, can look at subject
        or define a default one
    """

    languages_ratios = dict()
    words = [word.lower() for word in tokens]

    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements) # language score

    return max(languages_ratios, key=languages_ratios.get)

def get_language(tokens, stopwords):
    """
        Extract the language from an array of tokens, based on the stop words
        files given for the project
    """
    pass

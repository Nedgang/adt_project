#!/usr/bin/env python3

# -*- coding: utf8 -*-

# import
import nltk.stem.snowball

def stemme_list(source, language):

    if(language == "french"):
        stemmer = nltk.stem.snowball.FrenchStemmer()
    else:
        stemmer = nltk.stem.snowball.EnglishStemmer()

    stem_word = list()
    for word in source:
        stem_word.append(stemmer.stem(word))

    return stem_word

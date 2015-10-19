#!/usr/bin/env python3

# -*- coding: utf8 -*-

# import
import nltk.stem.snowball

# local import
# import lang_detection

def stemme_list(source):

    # if(lang_detection(source) == "french"):
    #     stemmer = nltk.stem.snowball.FrenchStemmer()
    # else:
    #     stemmer = nltk.stem.snowball.EnglishStemmer()

    stemmer = nltk.stem.snowball.FrenchStemmer()
    
    stem_word = list()
    for word in source:
        stem_word.append(stemmer.stem(word))

    return stem_word

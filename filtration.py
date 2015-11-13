#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This library allows to filter a set of terms, deleting non-valuable words using
a list of stop-words
"""

##########
# IMPORT #
##########
import glob
import os
import re

#############
# FUNCTIONS #
#############

def filtration(token, stopword, language):
    """
    Filter each token, depending on a stopword set and the language
    Return a list of string
    token = a list
    stopword = stopword object (cf stopwords.py)
    language = string (french or english)
    """
    word_ret = list()

    for word in token:
        # Check if the word is in the stopword list
        if __valid_word(word, stopword, language):
            word_ret.append(word)

    return word_ret


def __valid_word(word, stopword, language):
    """
    Check if the word is in the stopword list
    Return a boolean
    word = string
    stopword = stopword object (cf stopwords.py)
    language = string (french or english)
    """
    return (word not in stopword.get_stopword()[language]
            and word not in stopword.get_ponctuation()
            and not re.match("\d+", word))

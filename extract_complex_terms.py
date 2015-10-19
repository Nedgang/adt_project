#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyze a list of words, and search for complex terms.
Return a list of simple and complex terms.
"""

##########
# IMPORT #
##########
from collections import defaultdic

########
# MAIN #
########
def complexe_termes_extraction(list_words):
    """
    This function will analyze a list of words and search for complexe termes.
    Take a list in entry, with the words in the text order.
    Return a list, with simple and complex terms.
    """
    association_list = []
    #For each word in the list, we take the next one and save the combinaison
    # to make a count on it.
    for word_index in range(len(list_words)-1):
        association_list.append(
            (list_words[word_index], list_words[word_index+1]))
    # The count of each combinaison will be stocked in a dict.
    asso_number = __association_count(association_list)

#############
# FUNCTIONS #
#############
def __association_count(association_list):
    """
    Count each combinaison in a list of tuple, and return a dictionnary
    with the result.
    """
    number_comb = defaultdic(int)
    for combinaison in association_list:
        number_comb[combinaison] += 1
    return number_comb

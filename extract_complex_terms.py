#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyze a list of words, and search for complex terms.
Return a list of simple and complex terms.
"""

##########
# IMPORT #
##########
from collections import Counter

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

    # The count of each combinaison will be stocked in a dict
    asso_number = Counter(association_list)
    complex_terms = __complex_terms(asso_number)

    return complex_terms


#############
# FUNCTIONS #
#############
def __complex_terms(dic_combinaison, k=2):
    """
    Take a dictionnary containing each combinaison of termes and return those
    which are found k or more time (default k=2).
    It return a dict, containing each complex term is a key in string form, 
    and value is the numbre is presente in dic_combinaison.
    """
    # Remove all key isn't present upper than k, and replace key tuple by a
    # string
    return {" ".join(key):dic_combinaison[key] for key in
                    dic_combinaison if dic_combinaison[key] >= k}


def clean_term_list(list_words, complex_terms):
    """
    Take the basic set of terms and the list of complex terms.
    Return a list containing all the terms, complex and simple.
    """
    # We don't want to include simple terms already in complex terms
    print(complex_terms)


########
# TEST #
########
complexe_termes_extraction(["a", "la", "queue", "leu", "leu", "insuffisance",
                            "cardiaque", "queue", "supermarché", "insuffisance"
                            , "cardiaque", "diabète", "queue", "leu"])

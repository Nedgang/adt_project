#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyze a list of words and search for complex terms.
Return a list of simple and complex terms.
"""

##########
# IMPORT #
##########
from collections import Counter
from nltk.util import ngrams


########
# MAIN #
########
def complexe(list_words, complex_size=2, threshold=2):
    """
    This function will analyze a list of words and search for complexe terms.
    Take a list in entry, with the words in the text order.
    Return a dictionary, with complex terms and their occurences.
    """
    association_list = []

    # For each word in the list, we take the next one and save the combinaison
    association_list = ngrams(list_words, complex_size)

    # The count of each combinaison will be stored in a dict
    asso_number = Counter(association_list)

    # Remove combinations with score lower than threshold
    complex_terms = __filter_terms(asso_number, threshold)

    return complex_terms


def simple(list_words, threshold=1):
    """
    This function will analyze a list of words and search for complexe terms.
    Take a list in entry, with the words in the text order.
    Return a dictionary, with simple terms and their occurences.
    """

    # Count all simple terms and remove if lower than threshold
    return __filter_terms(Counter(list_words), threshold)


#############
# FUNCTIONS #
#############
def __filter_terms(dic_combinaison, threshold):
    """
    Take a dictionnary containing each combinations of terms and return those
    which are found k or more time (default k=2).
    It returns a dict, containing each complex term as a key <str>,
    and value is the number of occurence <int> in dic_combinaison.
    """
    # Remove all key with score lower than k, and replace key tuple by a
    # string
    return {__key2str(key): dic_combinaison[key] for key in
            dic_combinaison if dic_combinaison[key] >= threshold}


def __key2str(key):
    """
    Take a key and return in string format.
    """
    if type(key) is tuple:
        return " ".join(key)
    else:
        return key

def clean_term_list(list_words, complex_terms):
#########
# @TODO #
#########
    """
    Take the basic set of terms and the list of complex terms.
    Return a list containing all the terms, complex and simple.
    """
    # We don't want to include simple terms already in complex terms
    print(complex_terms)
#############
# END @TODO #
#############


########
# TEST #
########
if __name__ == "__main__":
    list_of_terms = ["a", "la", "queue", "leu", "leu", "insuffisance",
                     "cardiaque", "queue", "supermarché", "insuffisance",
                     "cardiaque", "diabète", "queue", "leu"]
    print(complexe(list_of_terms))
    print(simple(list_of_terms))

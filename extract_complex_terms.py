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
    #result = 
    clean_term_list(list_words, complex_terms)
    #print(result)

#############
# FUNCTIONS #
#############
def __complex_terms(dic_combinaison, k=2):
    """
    Take a dictionnary containing each combinaison of termes and return those
    which are found k or more time (default k=2).
    It return a list, containing each complex term in his string form.
    """
    # Return a list containing each tumple found k+ time
    cplxes_terms = list(filter(lambda x: dic_combinaison[x] >= k, dic_combinaison))
    # Now we transform each tuple in a string, to create the terms
    for i in range(len(cplxes_terms)):
        cplxes_terms[i] = cplxes_terms[i][0]+" "+cplxes_terms[i][1]
    return cplxes_terms

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

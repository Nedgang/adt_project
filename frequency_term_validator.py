#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
    TEST

    The idea is to filter our terms by their frequency in the language (FR only
    for testing purpose)

    If a term have an higher frequency in the mails than in the french language
    that means this term is probably specific


    TESTED:
        load_reference: load the reference file (frequency table for each words
        on wikipedia FR in 2008)
        filter_by_frequency: for a given term compare our frequency to the
        general frequency in french language
    TODO:
        try to use Pierre's work for real testing (score function already up-to-
        date)
        Maybe use this filter before stemming etc or stemm the reference too

    NOTES:
        Reference file full of shit (like punctuation) but, we dont care, the
        huge amount of terms in it compensate by far

    TEST
"""


import re
import math

def load_reference(freq_file):
    """
        Load the reference corpus, return a dict containing the frequency of a
        term in the corpus
    """

    # init
    freq = dict()
    global_term_count = 0

    # Get total number of words
    with open(freq_file, 'r') as INFILE:
        for line in INFILE: #not loading the whole file
            if len(line) > 1:
                # print(line)
                n, w = re.split("\s+", line.rstrip(),1)
                global_term_count += int(n)
                freq[w] = n #not a frequency yet

    # Frequency (we log it because it's really low)
    # N.B. we multiply by -1 for easier use later
    # Note that, doing log on <1 and *-1 will inverse the order
    # The highest frequency will be the closest to 0
    for key in freq.keys():
        freq[key] = int(freq[key])/int(global_term_count)

    return freq

def filter_by_frequency(query_dict, reference_dict, score_modifier = 1):
    """
        Compare the frequence of terms (keys) in query dict to the ones in the
        reference dict

        If the term have an higher frequency in the query_dict than in the
        reference_dict then we keep it, it must be specific to the field of our
        corpus, if not we delete it

        You can specify a score_modifier for a wider range in reference_dict
        It must be something like: 5% --> 1.05
    """

    keys_to_pop = list()

    for key in query_dict.keys():
        if key in reference_dict.keys():
            if query_dict[key] <= score_modifier*reference_dict[key]:
                keys_to_pop.append(key)

    if len(keys_to_pop) > 0:
        for key in keys_to_pop:
            query_dict.pop(key, None)

    return query_dict

# freq=load_reference("/home/jerome/Desktop/tableFrequenceWiki_2008_utf8.txt")
# print(freq["le"])
# print(freq["bioinformatique"])
# query_dict={"bioinformatique":120, "le":4.2}
# print(filter_by_frequency(query_dict, freq, 1.05))

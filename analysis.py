#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Usage:

Options:

Authors:
    MARIJON Pierre, PICARD DRUET David,  PIVERT Jérome.
"""

##########
# IMPORT #
##########
# EXISTANT LIBRARY
import glob
import sys

# SPECIFIC LIBRARY
# Our command line analyser/checker
import cli_parser
# Our tool to split text
import tokenization
# Used to remove words which are not terms
import filtration
# Extract mails differents parts
import mail_parser
# Terms stemming
import stemming
# Detect which language is used in the email
import language_detection
# Manage stop words
import stop_word
# Smart terms counter (both simple and complex terms)
import terms_counter
# Create stockage structure
import tag2terms

from collections import defaultdict

########
# MAIN #
########
def main(arg):
    """ Main function of analyse """

    # Read database
    tagterms = tag2terms.Tag2Terms()
    tagterms.read_file(arg["input"])

    # Just print tag
    if arg["print_tag"]:
        print_tag(tagterms)
        return 0

    # Get all terms is in tag
    if arg["all_terms"]:
        print_all_terms(tagterms, arg["query"], arg["threshold"])
        return 0

    # Terms is in some tag have bonus
    if arg["best_terms"]:
        print_best_terms(tagterms, arg["query"], arg["threshold"])
        return 0

    # Print just terms is in all tag
    if arg["strict_terms"]:
        print_strict_terms(tagterms, arg["query"], arg["threshold"])
        return 0

    # Print the keyword of database
    if arg["keywords"]:
        print_keywords(tagterms, arg["keywords"])
        return 0

def print_tag(tagterms):
    """ Print all tag in data base """

    for tag in sorted(tagterms.get_tag()):
        print(tag)


def print_all_terms(tagterms, query, threshold):
    """ Print all terms is in query tag """

    # Take all terms
    all_terms = dict()
    for tag in query:
        all_terms.update(tagterms.get_terms_score(tag))

    # Remove terms with score lower threshold
    selected_terms = {k: v for (k,v) in all_terms.items() if v > threshold}

    # Sorted terms by score
    sorted_terms = list()
    [sorted_terms.append((k,v)) for v,k in sorted([(v,k) for k,v in selected_terms.items()], reverse=True)]

    print(sorted_terms)


def print_best_terms(tagterms, query, threshold, bonus=1.5):
    """ If terms is presente in all tag increasse score """

    # Take all terms
    all_terms = list()
    for tag in query:
        all_terms.append(tagterms.get_terms_score(tag).keys())

    # If terms is in all_terms list we have bonus in enrich terms
    enrich_terms = defaultdict(int)
    for tag in arg["query"]:
        for terms in tagterms.get_terms_score(tag).keys():
            if terms in all_terms :
                enrich_terms[terms] += tagterms.get_terms_score(tag)[terms] * bonus
            else:
                enrich_terms[terms] += tagterms.get_terms_score(tag)[terms] * bonus


    # Remove terms with score lower threshold
    selected_terms = {k: v for (k,v) in enrich_terms.items() if v > threshold}

    # Sorted terms by score
    sorted_terms = list()
    [sorted_terms.append((k,v)) for v,k in sorted([(v,k) for k,v in selected_terms.items()], reverse=True)]

    print(sorted_terms)


def print_strict_terms(tagterms, query, threshold):
    """ Print just terms is in all tag query """

    # Find selected terms
    list_of_set = list()
    for tag in query:
        list_of_set.append(set(tagterms.get_terms(tag).keys()))
    keep_terms = set.intersection(*list_of_set)

    all_terms = dict()

    for tag in query:
        all_terms.update(tagterms.get_terms_score(tag))

    # Select terms if is in keep_terms and thresohld is upper threshold
    selected_terms = {k: v for (k,v) in all_terms.items() if k in keep_terms and v > threshold}

    # Sorte terms by score
    sorted_terms = list()
    [sorted_terms.append((k,v)) for v,k in sorted([(v,k) for k,v in selected_terms.items()], reverse=True)]

    print(sorted_terms)


def print_keywords(tagterms, n):
    """
        Print the n first keywords reprensenting the corpus
    """

    sorted_terms = list()
    # Get global score terms
    dict_global_terms = tagterms.get_global_score()

    # Sort terms by score
    [sorted_terms.append((k,v)) for v,k in sorted([(v,k) for k,v in dict_global_terms.items()], reverse=True)]

    # print just first terms of sorted list
    print(sorted_terms[0:n])


##########
# LAUNCH #
##########
if __name__ == "__main__":
    arg = cli_parser.analysis_read_args(sys.argv[1:])
    if(arg is None):
        sys.exit(1)

    main(arg)

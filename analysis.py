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


########
# MAIN #
########
def main(arg):
    """ Main function of analyse """

    tagterms = tag2terms.Tag2Terms()

    tagterms.read_file(arg["input"])

    terms_list = list()

    if arg["print_tag"]:
        print_tag(tagterms)
    
    if arg["all_terms"]:
        print_all_terms(tagterms, arg["query"], arg["threshold"])

def print_tag(tagterms):
    """ Print all tag in data base """

    for tag in sorted(tagterms.get_tag()):
        print(tag)


def print_all_terms(tagterms, query, threshold):
    """ Print all terms is in query tag """

    all_terms = dict()
    
    for tag in arg["query"]:
        all_terms.update(tagterms.get_terms(tag))

    sorted_terms = list()
    [sorted_terms.append((k,v)) for v,k in sorted([(v,k) for k,v in all_terms.items()], reverse=True)]

    selected_terms = [k for (k,v) in sorted_terms if v > threshold]

    
    print(selected_terms)


##########
# LAUNCH #
##########
if __name__ == "__main__":
    arg = cli_parser.analysis_read_args(sys.argv[1:])
    if(arg is None):
        sys.exit(1)

    main(arg)

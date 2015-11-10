#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This project extract terms (simples and complex), from a mail corpus.

Usage:
    ./__main__.py (--input=<repository>) (--output=<file>) [options]

Options:
    --help, -h                  Show help message.
    --input, -i=<repository>    The directory containing all data.
    --output, -o=<file>         The _ file with results.
    --stopword_fr=<file>        French stop words file. (default value include)
    --stopword_en=<file>        English stop words file.(default value include)

Authors:
    MARIJON Pierre, PICARD DRUET David,  PIVERT Jérôme.
"""

##########
# IMPORT #
##########
# EXISTANT LIBRARY
import glob
import nltk
import os
import sys

# SPECIFIC LIBRARY
# Our command line analyser/checker
import cli_parser
# Our tool to split text
import tokenization
# Used to remove words which are not terms
import filtration
# Extract mails differents parts
import mail_parser
# Terms racinisation
import stemming
# Detect wich language is used in the email.
import language_detection
# Manage stop words
import stop_word
# Smart terms counter (both simple and complex terms)
import terms_counter
# Create stockage structure.
import inverted_index


########
# MAIN #
########
def main(arg):

    stopword = stop_word.StopWord(arg["stopword_fr"], arg["stopword_en"])
    terms_ii = inverted_index.InvertedIndex()

    # Take all mail, and just mail
    for mail_path in get_mails(arg["input"]):

        # Read the mail
        mail = mail_parser.parse_mail(mail_path)

        # Tokenize and filter each field
        for key in ['body', 'subject']:  # key order is important
            mail[key] = tokenization.this_string(mail[key])

            if key == 'body':
                mail["lang"] = language_detection.get_language(
                    mail['body'], stopword.get_stopword())

            mail[key] = filtration.filtration(mail[key], stopword,
                                              mail["lang"])
            mail[key] = stemming.stemme_list(mail[key], mail["lang"])
            mail["complexe_terms_"+key] = terms_counter.complexe(mail[key])
            mail["simple_terms_"+key] = terms_counter.simple(mail[key])

        # Write mail
        jsonout_name = arg["output"]
        jsonout_name += mail["name"]
        jsonout_name += ".json"
        terms_ii.add_mail(mail)

        mail_parser.write_json(mail, jsonout_name)


#############
# FUNCTIONS #
#############
def get_mails(arg):
    """
    This function return a set of mails contained in a directory.
    arg = directory path.
    """
    for directory in glob.glob(arg+"/*"):
        for mail in glob.glob(directory+"/*"):
            if not mail.endswith(".txt"):
                yield mail

##########
# LAUNCH #
##########
if __name__ == "__main__":
    arg = cli_parser.read_arg(sys.argv)
    if(arg is None):
        sys.exit(1)

    main(arg)

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
    MARIJON Pierre, PICARD DRUET David,  PIVERT Jérome.
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
# add comment
import tag2terms

########
# MAIN #
########
def main(arg):

    stopword = stop_word.StopWord(arg["stopword_fr"], arg["stopword_en"])
    tagterms = tag2terms.Tag2Terms()

    # Take all mail, and just mail
    for mail_path in get_mails(arg["input"]):

        # Read the mail
        mail = mail_parser.parse_mail(mail_path)

        # Determinate language of mail
        mail["lang"] = language_detection.get_language(mail['body'],
                                                       stopword.get_stopword())

        # Tokenize filter and stemme body and subject
        for field in ('body', 'subject'):
            mail[field] = stemming.stemme_list(
                filtration.filtration(
                    tokenization.this_string(mail[field]),
                    stopword,
                    mail["lang"]),
                mail["lang"])

        # Compute simple and complex terms for body
        mail['body_terms'] = terms_counter.complexe(mail['body'])
        mail['body_terms'].update(terms_counter.simple(mail['body']))

        # Compute simple terms for subject
        mail['subject_terms'] = terms_counter.simple(mail['subject'])

        # Write mail
        jsonout_name = arg["output"]
        jsonout_name += mail["name"]
        jsonout_name += ".json"

        # add this mail in tag2terms
        tagterms.add_mail(mail)

        mail_parser.write_json(mail, jsonout_name)

    # Use mail_parser.write_json for no mail but is very usefule function
    tagterms.serialize(arg["output"] + "tag2terms.json")

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

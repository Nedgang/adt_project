#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""

"""

##########
# IMPORT #
##########
import glob
import nltk
import os
import sys

import cli_parser
import tokenization
import filtration
import mail_parser
import stemming
import language_detection
import stop_word
import terms_counter
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
        for key in ['body', 'subject']:  # the order of key is important
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

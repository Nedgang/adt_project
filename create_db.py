#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This project extract terms (simples and complex) from a mail corpus, group them
by families, show the trends...

Usage:
    ./create_db.py (--input=<repository>) (--output=<file>) [options]

Options:
    --help, -h                  Show help message.
    --input, -i=<repository>    The directory containing all data.
    --output, -o=<file>         The _ file with results.
    --stopword_fr=<file>        French stop words file. (default value include)
    --stopword_en=<file>        English stop words file.(default value include)
    --debug                     Activate debug mode

Authors:
    MARIJON Pierre, PICARD DRUET David, PIVERT Jérome.
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
    """ Main function of email parser """

    stopword = stop_word.StopWord(arg["stopword_fr"], arg["stopword_en"])
    tagterms = tag2terms.Tag2Terms()

    # Take all mail, and just mail
    for mail_path in get_mails(arg["input"]):

        # Read the mail
        mail = mail_parser.parse_mail(mail_path)

        # Determine language of mail
        mail["lang"] = language_detection.get_language(mail['body'],
                                                       stopword.get_stopword())

        # Tokenize, filter and stem body and subject
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

        # Write result of email parsing in file just if debug mode is activate
        if arg["debug"]:
            mail_parser.write_json(mail, jsonout_name)

    # Store result of analysis
    tagterms.compute()
    tagterms.serialize(arg["output"] + "tag2terms")


#############
# FUNCTIONS #
#############
def get_mails(arg):
    """
    This function return a set of mails contained in a directory
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
    arg = cli_parser.create_db_read_arg(sys.argv[1:])
    if(arg is None):
        sys.exit(1)

    main(arg)

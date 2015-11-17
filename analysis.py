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

##########
# LAUNCH #
##########
if __name__ == "__main__":
    arg = cli_parser.analysis_read_args(sys.argv[1:])
    if(arg is None):
        sys.exit(1)

    main(arg)

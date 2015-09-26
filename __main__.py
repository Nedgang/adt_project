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

########
# MAIN #
########
def main(arg):
    for mail in get_mails(arg["input"]):
        print(mail)


#############
# FUNCTIONS #
#############
def get_mails(arg):
    for directory in glob.glob(arg+"/*"):
        for mail in glob.glob(directory+"/*"):
            yield mail

##########
# LAUNCH #
##########
if __name__ == "__main__":
    arg = cli_parser.read_arg(sys.argv)
    main(arg)

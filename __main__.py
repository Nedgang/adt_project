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

########
# MAIN #
########
def main(arg):

    stopword = stop_word.StopWord(arg["stopword_fr"],
                                 arg["stopword_en"])
    
    # Take all mail, and just mail
    for mail_path in get_mails(arg["input"]):

        # Read the mail
        mail = mail_parser.parse_mail(mail_path)

        # Tokenize and filter each field
        for key in ['body', 'subject']:
            mail[key] = tokenization.this_string(mail[key])

            if key == 'body':
                mail["lang"] = language_detection.get_language(mail['body'], stopword.get_stopword())

            mail[key] = filtration.filtration(mail[key], stopword, mail["lang"])
            mail[key] = stemming.stemme_list(mail[key])

        # Write mail
        jsonout_name = arg["output"]
        jsonout_name += os.path.dirname(mail_path).split('/').pop() + '-'
        jsonout_name += os.path.splitext(os.path.basename(mail_path))[0]
        jsonout_name += ".json"

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
    if(arg == None):
        sys.exit(1)

    main(arg)

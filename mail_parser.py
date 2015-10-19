#!/usr/bin/env python3

# -*- coding: utf8 -*-

import os, sys
from email.parser import Parser
import json
import re

def parse_mail(file_in):
    """
        Extract Subject & Body of mail file
        headers must be RFC 2822 style
    """

    # filename_out = os.path.splitext(os.path.basename(file_in))[0] + ".json"
    # infile_path = os.path.dirname(file_in)
    # dirname = infile_path.split('/').pop()
    #
    # PATH_out = infile_path + '/' + dirname + '_' + filename_out

    with open(file_in, 'r') as INFILE:
        raw_mail = Parser().parse(INFILE)
        formated_mail = {
                            "body":     raw_mail.get_payload(),
                            "subject":  raw_mail['subject'],
                        }

    reg = re.compile("[^@|\s]+@[^@]+\.[^@|\s]+") # black magic
    formated_mail['body'] = re.sub(reg, "",formated_mail['body']) # remove email

    return formated_mail

def write_json(dico, fileout):
    """
        Write dict into json-styled file
        Je collectionne les canards...
        ... vivants !
    """
    with open(fileout, "w") as OUTFILE:
        json.dump(dico, OUTFILE, ensure_ascii=False)

parse_mail(sys.argv[1])

#!/usr/bin/env python3

# -*- coding: utf8 -*-

import os
import sys
from email.parser import Parser
import json
import re


def parse_mail(file_in):
    """
        Extract Subject & Body of mail file
        headers must be formatted as a block of RFC 2822 style
    """

    with open(file_in, 'r') as INFILE:
        raw_mail = Parser().parse(INFILE)
        formated_mail = {
            "body":     raw_mail.get_payload(),
            "subject":  raw_mail['subject'],
        }

    # small correction of text, remove email adresses in the text
    reg = re.compile("[^@|\s]+@[^@]+\.[^@|\s]+")  # black magic
    formated_mail['body'] = re.sub(reg, "", formated_mail['body'])

    date = os.path.dirname(file_in).split('/').pop() + '-'
    name = os.path.splitext(os.path.basename(file_in))[0]
    formated_mail['name'] = date+name

    return formated_mail


def write_json(dico, fileout):
    """
        Write dict into json-styled file
        Je collectionne les canards...
        ... vivants !
    """
    with open(fileout, "w") as OUTFILE:
        json.dump(dico, OUTFILE, ensure_ascii=False)


def correct_mail(file_in):
    """
        Remove all blank lines in mail files, it fucks-up the parsing if not
    """
    new_body = ""
    with open(file_in, 'r') as INFILE:
        # select only non-blank lines, use generator to avoid memory storage
        for line in (l for l in INFILE if(len(l.strip()) > 1)):
            new_body += line
    # regenerate the mail file
    with open(file_in, 'w') as INFILE:
        INFILE.write(new_body)

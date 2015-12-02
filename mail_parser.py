#!/usr/bin/env python3
# -*- coding: utf8 -*-

##########
# IMPORT #
##########
import os
import sys
import email
import json
import re


def parse_mail(file_in):
    """
        Extract Subject & Body of mail file
        headers must be formatted as a block of RFC 2822 style

        input:  file path
        output: dict
    """

    # We open the file and then divide it in different parts.
    with open(file_in, 'rb') as INFILE:
        raw_mail = email.message_from_binary_file(INFILE)
        charset = raw_mail.get_charsets()[0]
        formated_mail = {
            "body": raw_mail.get_payload(decode=True).decode(charset),
            "subject": str(email.header.make_header(email.header.decode_header(raw_mail["Subject"])))
,
            "encoding": raw_mail['content-type']
        }

    date = os.path.dirname(file_in).split('/').pop() + '-'
    name = os.path.splitext(os.path.basename(file_in))[0]
    formated_mail['name'] = date+name

    formated_mail = dc_remove_adresses(formated_mail)
    formated_mail = dc_remove_url(formated_mail)

    return formated_mail

def write_json(dico, fileout):
    """
        Write dict into json file

        input:  dict
        output: json file
    """
    with open(fileout, "w") as OUTFILE:
        json.dump(dico, OUTFILE, ensure_ascii=False)



########################
# CORRECTION FUNCTIONS #
########################
# 2 types of corrections, defined by prefix 'fc' or 'dc'
# fc: FILE_CORRECTION: alterate the original file
# dc: DATA_CORRECTION: alterate the dictionnary containing the body+subject


# FILE_CORRECTION
def fc_remove_blank_lines(file_in):
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

# DATA_CORRECTION
def dc_remove_adresses(dict):
    '''
        Small correction of text, remove email adresses in the mail body
    '''
    reg = re.compile("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_"
                    "`{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\."
                    "|\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)") # black magic
    dict['body'] = re.sub(reg, "", dict['body'])

    return dict

def dc_remove_url(dict):
    '''
        Small correction of text, remove URLs in the mail body
        This regexp isn't an optimized one (see https://mathiasbynens.be/demo/url-regex)
    '''
    reg = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+") # ultra black magic
    dict['body'] = re.sub(reg, "", dict['body'])

    return dict

def dc_correct_body_encoding(dict):
    '''
        Encoding correction for mail body, we want an utf-8 encoded text from
        the given charset in the mail
    '''
    # Extract the original charset of mail
    reg = re.compile('charset=([^\s;]+)')
    encoding = re.search(reg, dict['encoding']).group(1)

    # Convert <str> to <bytes> then decode (default to unicode)
    # (Python3 requirement for encoding/decoding operation)
    bstr = bytes(dict['body'])
    dict['body'] = bstr.decode(encoding)

    return dict

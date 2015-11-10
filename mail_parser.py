#!/usr/bin/env python3

# -*- coding: utf8 -*-


##########
# IMPORT #
##########
import os, sys
from email.parser import Parser
import email.header
import json
import re


def parse_mail(file_in):
    """
        Extract Subject & Body of mail file
        headers must be formatted as a block of RFC 2822 style

        input:  file
        output: dict
    """

    with open(file_in, 'r') as INFILE:
        raw_mail = Parser().parse(INFILE)
        formated_mail = {
            "body":     raw_mail.get_payload(),
            "subject":  raw_mail['subject'],
        }


    date = os.path.dirname(file_in).split('/').pop() + '-'
    name = os.path.splitext(os.path.basename(file_in))[0]
    formated_mail['name'] = date+name

    return formated_mail


def write_json(dico, fileout):
    """
        Write dict into json-styled file
        Je collectionne les canards...
        ... vivants !

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
        Sometimes, sacrificing goats to Satan isn't enough to get your regexp,
        sometimes you also need a bit of unicorn's power
    '''
    reg = re.compile("^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$") # ultra black magic
    dict['body'] = re.subn(reg, "", dict['body'])[0]

    return dict


#print(dc_remove_adresses(parse_mail("test/test_mail/1.recoded")))

'''
    with open(file_in, 'a') as s_file:
        ugly_subject = msg.get('subject', None)

        # No subject in header
        if ugly_subject is not None:

            # Multiple spaces (2)
            ugly_subject = re.sub('[ ]{2}', '', ugly_subject)
            r = decode_header(ugly_subject)

            # No decoding required => [(entire chain)]
            if len(r) > 1:
                # Subject does not meet the RFC2047 :-(
                try:
                    clean_subject = ''.join(txt.decode(enc or "utf-8")
                                            for txt, enc in r)
                except:
                    clean_subject = "ERROR: " + email_file_path + \
                                    ";" + ugly_subject
                finally:
                    s_file.write(clean_subject + '\n')

'''

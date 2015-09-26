#!/usr/bin/env python3

# -*- coding: utf8 -*-

# import
import nltk.tokenize

def this_file(filename):
    reg_words = r'''(?x)
    \d+(\.\d+)?\s*%
    | 's
    | \w'
    '''
    # les pourcentages, l'appartenance anglaise 's,
    # les contractions d', l', j', t', s'

    # Version unicode
    reg_words += u"| \w\u2019"
    reg_words += u"|\w+|[^\w\s]"

    tok = nltk.tokenize.RegexpTokenizer(reg_words)

    with open(filename, "r") as content:
        return tok.tokenize(content.read())

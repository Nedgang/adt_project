#!/usr/bin/env python3
# -*- coding: utf8 -*-

# import
import nltk.tokenize


def this_string(string):
    """
    Take a string and return a list of token.
    """
    reg_words = r'''(?x)
    \d+(\.\d+)?\s*%
    | 's
    | \w'
    | \w+([-']\w+)*
    '''
    # les pourcentages, l'appartenance anglaise 's,
    # les contractions d', l', j', t', s'

    # Version unicode
    reg_words += u"| \w\u2019"
    reg_words += u"|\w+|[^\w\s]"

    tok = nltk.tokenize.RegexpTokenizer(reg_words)

    return tok.tokenize(str(string))

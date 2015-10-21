#!/usr/bin/env python3

# -*- coding: utf8 -*-

# import
import glob
import os
import re


def filtration(tok_content, stopword, language):

    word_ret = list()

    for word in tok_content:
        if __valid_word(word, stopword, language):
            word_ret.append(word)

    return word_ret


def __valid_word(word, stopword, language):
    return word not in stopword.get_stopword()[language] and word not in stopword.get_ponctuation() and not re.match("\d+", word)


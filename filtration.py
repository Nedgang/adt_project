#!/usr/bin/env python3

# -*- coding: utf8 -*-

# import
import glob
import os

def filtration(tok_content, stopword, language):

    word_ret = list()

    for word in tok_content:
        if word not in stopword.get_stopword()[language] and word not in stopword.get_ponctuation() :
            word_ret.append(word)
            
    return word_ret

          

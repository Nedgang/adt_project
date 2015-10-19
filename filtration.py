#!/usr/bin/env python3

# -*- coding: utf8 -*-

# import
import glob
import os

def filtration(tok_content, stopword, language):

    word_ret = list()

    print(stopword.get_ponctuation())
    for word in tok_content:
        if word not in stopword.get_stopword()[language]:
            word_ret.append(word)
            
    return word_ret

          

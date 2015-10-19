#!/usr/bin/env python3

# -*- coding: utf8 -*-

# import
import glob
import os
import blist

class Filtration:

    def __init__(self, filter_dir) :
        self.word_filter = self.__readfilter(filter_dir)

    def __call__(self, tok_content):

            word_ret = list()

            for word in tok_content:
                if word not in self.word_filter:
                    word_ret.append(word)
                    
                    return word_ret


    def __readfilter(self, filter_dir):
        """Warning this is private function didn't use please kiss"""

        word_filter = blist.sortedlist()
        for filtr in glob.glob(filter_dir+"/*"):
            print(filtr)
            if os.path.isfile(filtr):
                with open(filtr, "r") as filtr_h:
                    for word in filtr_h:
                        word_filter.add(word)
    
        return word_filter                

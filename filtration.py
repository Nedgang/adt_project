#!/usr/bin/env python3

# -*- coding: utf8 -*-

# import
import glob
import os
import blist


def filtration(tok_content, filter_dir):
    word_filter = __readfilter(filter_dir)
    world_ret = list()

    for word in tok_content:
        if word in word_filter:
            world_ret.append(word)

    return word


def __readfilter(filter_dir):
    """Warning this is private function didn't use please kiss"""
    word_filter = blist.sortedlist()
    for filtr in glob.glob(filter_dir):
        if os.isfile(filtr):
            with open(filtr, "r") as filtr_h:
                for word in filtr_h:
                    word_filter.append(word)

#!/usr/bin/env python3

# -*- coding: utf8 -*-

# std import
import json
import math
from collections import defaultdict

class Tag2Terms:

    def __init__(self):
        self.__tag2terms = defaultdict(lambda: defaultdict(int))
        self.__dfidf = defaultdict(lambda: defaultdict(float))
        
    def add_mail(self, mail):
        for tag in mail["subject_terms"]:
            for terms in mail["body_terms"].keys():
                self.__tag2terms[tag][terms] += mail["body_terms"][terms]

    def serialize(self, basename):
        with open(basename+"_count.json", "w") as out:
            json.dump(self.__tag2terms, out, ensure_ascii=False)

        with open(basename+"_score.json", "w") as out:
            json.dump(self.__dfidf, out, ensure_ascii=False)
            
    def read_file(self, basename):
        with open(basename+"_count.json", "r") as infile:
            self.__tag2terms.update(json.load(infile)) 

        with open(basename+"_score.json", "r") as infile:
            self.__dfidf.update(json.load(infile)) 

            
    def get_tag(self):
        return self.__tag2terms.keys()
            
    def get_terms(self, tag):
        return self.__tag2terms[tag]

    def compute(self):
        for tag in self.__tag2terms.keys():
            for terms in self.__tag2terms[tag].keys():
                tf = self.__tag2terms[tag][terms]
                df = self.__df4terms(terms)
                self.__dfidf[tag][terms] = math.log(tf/df)
                
    def __df4terms(self, terms):
        ret = 0
        for tag in self.__tag2terms.keys():
            if terms in self.__tag2terms[tag]:
                ret += 1

        return ret

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
        self.__terms_global_counter = defaultdict(int)

    def add_mail(self, mail):
        for tag in mail["subject_terms"]:
            for terms in mail["body_terms"].keys():
                self.__tag2terms[tag][terms] += mail["body_terms"][terms]

        for terms in mail["body_terms"].keys():
            self.__terms_global_counter[terms] += mail["body_terms"][terms]
        for terms in mail["subject_terms"]:
            self.__terms_global_counter[terms] += mail["subject_terms"][terms]

    def serialize(self, basename):
        with open(basename+"_count.json", "w") as out:
            json.dump(self.__tag2terms, out, ensure_ascii=False)

        with open(basename+"_score.json", "w") as out:
            json.dump(self.__dfidf, out, ensure_ascii=False)

        with open(basename+"_gcounter.json", "w") as out:
            json.dump(self.__terms_global_counter, out, ensure_ascii=False)

    def read_file(self, basename):
        with open(basename+"_count.json", "r") as infile:
            self.__tag2terms.update(json.load(infile))

        with open(basename+"_score.json", "r") as infile:
            self.__dfidf.update(json.load(infile))

        with open(basename+"_gcounter.json", "r") as infile:
            self.__terms_global_counter.update(json.load(infile))

    def get_tag(self):
        return self.__tag2terms.keys()

    def get_terms(self, tag):
        return self.__tag2terms[tag]

    def get_tag_score(self):
        return self.__dfidf.keys()

    def get_terms_score(self, tag):
        return self.__dfidf[tag]

    def get_global_score(self):
        return self.__terms_global_counter

    def compute(self):
        """
            Compute the score of a term for a given tag

            Score is calculated from the number of occurence of the given term
            in the corpus and the number of occurence of this term in the
            subjects of the corpus

            Score is:
                "the number of occurence of a term IN the tag"
                -------------------------------------------------
                "the number of occurence of a term in the corpus"
        """
        for tag in self.__tag2terms.keys():
            for terms in self.__tag2terms[tag].keys():
                tag_occur = self.__tag2terms[tag][terms]
                global_occur = self.__terms_global_counter[terms]
                self.__dfidf[tag][terms] = tag_occur/global_occur

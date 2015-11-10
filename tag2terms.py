#!/usr/bin/env python3

# -*- coding: utf8 -*-

# std import
import json
from collections import defaultdict

class Tag2Terms:

    def __init__(self):
        self.__tag2terms = defaultdict(lambda: defaultdict(int))

    def add_mail(self, mail):
        for tag in mail["subject_terms"]:
            for terms in mail["body_terms"].keys():
                self.__tag2terms[tag][terms] += mail["body_terms"][terms]

    def serialize(self, filename):
        with open(filename, "w") as out:
            json.dump(self.__tag2terms, out, ensure_ascii=False)

    def read_file(self, filename):
        with open(filename, "r") as infile:
            self.__tag2terms.update(json.load(infile)) 
        

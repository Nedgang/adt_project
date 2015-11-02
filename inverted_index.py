#!/usr/bin/env python3

# -*- coding: utf8 -*-

# import


class InvertedIndex:

    def __init__(self):
        self.index = dict()

    def add_mail(self, mail):
        for key in ["simple_terms_body", "complexe_terms_body"]:
            for terms in mail[key]:
                if terms in self.index.keys():
                    self.index[terms].append((mail["name"], mail[key][terms]))
                else:
                    self.index[terms] = list()
                    self.index[terms].append((mail["name"], mail[key][terms]))

    def terms(self):
        for terms in self.index.keys():
            yield terms

    def get_terms(self):
        return self.index.keys()

    def file_counter(self, terms):
        for val in self.index[terms]:
            yield val

    def get_file_counter(self, terms):
        return self.index.values()

    def file(self, terms):
        for val in file_counter(terms):
            yield val[0]

    def counter(self, terms):
        for val in file_counter(terms):
            yield val[1]

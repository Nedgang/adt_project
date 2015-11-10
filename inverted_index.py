#!/usr/bin/env python3

# -*- coding: utf8 -*-

# import


class InvertedIndex:

    def __init__(self):
        self.index = dict()

    def add_mail(self, mail):
        for key in ["simple_terms_body", "complexe_terms_body"]:
            for terms in mail[key]:
                if terms not in self.index.keys():
                    self.index[terms] = dict()
                    self.index[terms][mail["name"]] = mail[key][terms]
                else:
                    self.index[terms][mail["name"]] = mail[key][terms]

    def terms(self):
        for terms in self.index.keys():
            yield terms

    def get_terms(self):
        return self.index.keys()

    def files(self, terms):
        for val in self.index[terms].keys():
            yield val

    def get_files(self, terms):
        return self.index[terms].keys()

    def val(self, terms, filename):
        return self.index[terms][filename]


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


#!/usr/bin/env python3

# -*- coding: utf8 -*-


class StopWord:

    def __init__(self, french, english):
        self.__stopword = dict()
        if not french and not english:

            from nltk.corpus import stopwords
            self.__stopword["english"] = set(stopwords.words("english"))
            self.__stopword["french"] = set(stopwords.words("french"))

        else:

            self.__stopword["english"] = self.__readfilter(english)
            self.__stopword["french"] = self.__readfilter(french)

        self.__ponctuation = (",", ";", ".", ":", "(", ")", "\"",
                              "\'", "<", ">", "=", "«", "»", "#")

    def __readfilter(self, filename):
        """Warning this is private function didn't use please kiss"""

        word_filter = set()
        with open(filename, "r") as filtr_list:
            for word in filtr_list:
                word_filter.add(word)

        return word_filter

    def get_stopword(self):
        return self.__stopword

    def get_ponctuation(self):
        return self.__ponctuation

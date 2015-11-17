#!/usr/bin/env python3
# -*- coding: utf8 -*-

# nltk tool for stemming
import nltk.stem.snowball


def stemme_list(source, language):
    """
    This function take list of words from a language and return stemmed forms

    source: list of words
    language: the string "french" or "english"

    Return a list of stemmed words.
    """
    if(language == "french"):
        stemmer = nltk.stem.snowball.FrenchStemmer()
    else:
        stemmer = nltk.stem.snowball.EnglishStemmer()

    stem_word = list()
    # We take each words in the list, and stem it into the stem_word list.
    for word in source:
        stem_word.append(stemmer.stem(word))

    return stem_word


########
# TEST #
########
if __name__ == "__main__":
    list_of_terms = ["a", "la", "queue", "leu", "leu", "insuffisance",
                     "cardiaque", "queue", "supermarché", "insuffisance",
                     "cardiaque", "diabète", "queue", "leu"]
    print(list_of_terms)
    print(stemme_list(list_of_terms, "french"))

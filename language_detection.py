#!/usr/bin/env python3

# -*- coding: utf8 -*-


def get_language(tokens, stopwords):
    """
    Extract the language from an array of tokens, it is based on stop words
    It takes two args:
        tokens    -> list of words to check the language
        stopwords -> dict of set: {lang : set(language,specific,stop,words)}

    It sets a score to a language by intersection between tokens & stopwords
    by language. The highest score is considered as the main language of
    the list and is returned.

    improvement: if 2 language have equal score, can look at subject (too
    small for good detection) or define a default value
    """

    languages_ratios = dict()

    words = [str(word).lower() for word in tokens]
    words_set = set(words)

    for language in stopwords.keys():
        common_elements = words_set.intersection(stopwords[language])

        languages_ratios[language] = len(common_elements)  # language score

    return max(languages_ratios, key=languages_ratios.get)

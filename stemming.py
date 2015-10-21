#!/usr/bin/env python3

# -*- coding: utf8 -*-

# import
import nltk.stem.snowball

def stemme_list(source, language):

    if(language == "french"):
        stemmer = nltk.stem.snowball.FrenchStemmer()
    else:
        stemmer = nltk.stem.snowball.EnglishStemmer()

    stem_word = list()
    for word in source:
        stem_word.append(stemmer.stem(word))

    return stem_word


########
# TEST #
########
if __name__ == "__main__":
    list_of_terms = ["a", "la", "queue", "leu", "leu", "insuffisance",
                     "cardiaque", "queue", "supermarché", "insuffisance"
                     , "cardiaque", "diabète", "queue", "leu"]
    print(list_of_terms)
    print(stemme_list(list_of_terms, "french"))
    

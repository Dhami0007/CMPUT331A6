#!/usr/bin/env python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023 <<Jaspreet Singh Dhami>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
Problem 1
"""

from sys import flags

def ngramsFreqsFromFile(textFile: str, n: int) -> dict:
    """
    textFile: 'wells.txt'
    """
    file = open(textFile, "r")
    input = file.read()
    file.close()

    n_gram_dict = dict()
    idx = 0
    length = len(input)
    while (idx + (n - 1)) <= (length - 1):  # This condition since it will stop after looking at the last n chars in the text
    # This is updating the dictionary with the occurences of all the ngrams in the text
        target_gram = input[idx:idx+n]
        n_gram_dict[target_gram] = n_gram_dict.get(target_gram,0) + 1
        idx += 1
    
    total_n_grams = length - (n - 1)
    
    for key in n_gram_dict.keys():
    # This is updating the dictionary with frequencies of the ngrams in the text
        n_gram_dict[key] = n_gram_dict[key]/total_n_grams
    
    return n_gram_dict

def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    ngramsFreqsFromFile("wells.txt", 1)

if __name__ == "__main__" and not flags.interactive:
    test()

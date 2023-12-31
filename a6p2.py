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
Problem 2
"""

from sys import flags

def keyScore(mapping: dict, ciphertext: str, frequencies: dict, n: int) -> float:
    decipherment = ""
    for c in ciphertext:
        if c.isalpha():
            decipherment += mapping[c]
        else:
            decipherment += c
    
    score =  0

    for n_gram in frequencies.keys():
        c = len(decipherment.split(n_gram)) - 1 # If it got split into 2 parts, there is 1 n_gram. If into 3 then there are 2 n_grams and so on
        f = frequencies[n_gram]
        score += c*f
    
    return score

def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking

if __name__ == "__main__" and not flags.interactive:
    test()






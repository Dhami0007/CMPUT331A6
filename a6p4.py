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
Problem 4
"""
from sys import flags
from a6p3 import bestSuccessor
from a6p1 import ngramsFreqsFromFile

ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


def freqDict(ciphertext: str) -> dict:
    """
    This function is from a5p1.py
    Analyze the frequency of the letters
    """
    res_dict = dict()
    for c in ciphertext:
        c = c.upper()
        if c in ETAOIN:
            res_dict[c] = res_dict.get(c,0) + 1
    
    freq_tracker = [0 for _ in range(len(res_dict.keys()))]     # This will be used to make the encryption valid

    val_order = list(res_dict.values())
    val_order.sort(reverse=True)
    alpha_order = list(res_dict.keys())
    alpha_order.sort()
    # This will val_order the number of occurences in descending val_order
    for key in alpha_order:
        val = res_dict[key]
        idx = val_order.index(val)
             
        freq_tracker[idx] += 1      
        # We will be adding this because val_order.index() will give us index of the first occurence, 
        # then this will make it point to the actual index after that
        idx += (freq_tracker[idx] - 1)      
        
        # Overwriting the keys
        res_dict[key] = ETAOIN[idx]
    
    return res_dict

def freqDecrypt(mapping: dict, ciphertext: str) -> str:
    """
    This code is from a5p1.py
    Apply the mapping to ciphertext
    """
    result = ""

    for c in ciphertext:
    # This loop is putting the diphered text together piece by piece
        c = c.upper()
        if c in ETAOIN:
        # Handling alphabets
            result += mapping[c]
        else:
        # Handling non alphabets
            result += c

    return result

def breakSub(cipherFile: str, textFile: str, n: int) -> None:
    """
    Inputs:
        cipherFile: 
            'text_finnegan_cipher.txt' for implementation
            'text_cipher.txt' for submission
        textFile: 'wells.txt'
    Outputs:
        'text_finnegan_plain.txt' for implementation
        'text_plain.txt' for submission
    """
    
    file = open(cipherFile,"r")
    cipher = file.read()
    file.close()

    mapping = freqDict(cipher)
    
    n_gram = ngramsFreqsFromFile(textFile, n)

    mapping = bestSuccessor(mapping, cipher, n_gram, n)
    next_best_mapping = bestSuccessor(mapping, cipher, n_gram, n)
    while mapping != next_best_mapping:
        mapping = next_best_mapping.copy()
        next_best_mapping = bestSuccessor(next_best_mapping, cipher, n_gram, n)

    decipherment = freqDecrypt(mapping, cipher)

    file = open("text_plain.txt", "w")
    file.write(decipherment)
    file.close()

def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    breakSub("text_cipher.txt", "wells.txt", 3)

if __name__ == "__main__" and not flags.interactive:
    test()
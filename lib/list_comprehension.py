#!/usr/bin/env python3
def return_evens(num_list):
    # Use list comprehension to select only even numbers
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    # Use list comprehension to append "!" to each sentence
    return [sentence + "!" for sentence in sentence_list]

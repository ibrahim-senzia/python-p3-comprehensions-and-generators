#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n % 2 ==0]
    if not evens:
        return []
    return evens

return_evens([1,2,3,4,5,6,7,8])

def make_exclamation(sentence_list):
    updated_list = [char + ('!') for char in sentence_list]
    if not updated_list:
        return []
    return updated_list

make_exclamation(['Hello', 'Marrie'])


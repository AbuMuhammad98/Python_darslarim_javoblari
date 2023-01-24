# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:19:44 2023

@author: AbuMuhammad
"""

def number_to_string(num):
    # Return a string of the number here!
    return str(num)

num_to_string = lambda n: str(n)


def even_or_odd(number):
    if number%2==0:
        return 'even'
    else:
        return 'odd'


def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'
    
print(bool_to_word(True))


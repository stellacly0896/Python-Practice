"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""


def find_it(seq):
    count_dict = dict((i,seq.count(i)) for i in set(seq))
    for k,v in count_dict.items():
        if v % 2 != 0:
            return k

#sample, simply use:

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

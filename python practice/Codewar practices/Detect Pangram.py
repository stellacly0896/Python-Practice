"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
Ignore numbers and punctuation.

"""

def is_pangram(string):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    string = string.lower()

    for s in string:
        letters = letters.replace(s,"")

    if len(letters) == 0:
        return True
    else:
        return False


#sample1:
import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
"""
First things first is we generate a string of all the lowercase letters in the alphabet by using:
string.ascii_lowercase
Then we convert that string into a set so we can compare it to the string that the kata provides use by using:
set(string.ascii_lowercase)
From there, we compare the length of the alphabet to the length of the string provided after we converted it to a set.
The set conversion is very important here, sets do not have duplicate elements, so by converting the string into a set we remove any duplicates, this allows us to compare the length to the alphabet.
We use the less than or equal to comparison (<=) because if the string is larger then the set, that means the string contains all the letters of the alphabet and extra characters ontop of that, obviously those extra characters can't be letters so they must be symbols.
this comparison is going to give us a true or false value back, so we use return to get that value.
"""

#sample2:
def is_pangram(s):
    s = s.lower()
    for char in "qwertyuiopasdfghjklzxcvbnm":
        if char not in s:
            return False
    return True

"""
import string
string.ascii_lowercase will generate a string of lowercase letters in alphabet

"""

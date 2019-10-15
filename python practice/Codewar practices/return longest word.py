"""Write a Python function that takes a list of words and returns the length of the longest one and the word itself.
"""

def longest_word(words):
    lst = []
    for word in words:
        lst.append((len(word),word))
    lst.sort()
    return lst[-1][1]

print(longest_word(["a","ab","abc"]))

#list是可以append()这样的pair的

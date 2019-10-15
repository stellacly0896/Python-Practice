"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(nums):
    #split the whole number into individuals
    l = [int(i) for i in str(nums)]
    l.reverse()
    exp = []
    for i in range(len(l)):
        if l[i] != 0: #don't want to include 0 in the final results
            number = l[i] * 10 ** i
            exp.append(str(number)) # convert int objects into strings so that we can use .join()
    exp.reverse()
    return " + ".join(exp)


#sample

def expanded_form(num):
    a = len(str(num))
    b = []
    for i,j in enumerate(str(num)):
        if j != '0':
            b.append(j+'0'*(a-i-1))
    return ' + '.join(b)


def expanded_form(num):
    result = ''
    for i, char in enumerate(str(num)):
        if char != '0':
            if i != 0:
              result += " + "
            result += char
            for i in str(num)[i+1:]:
                result += '0'
    return result

"""
enumerate():

>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]


>>>seq = ['one', 'two', 'three']
>>> for i, element in enumerate(seq):
...     print i, element
...
0 one
1 two
2 three
"""

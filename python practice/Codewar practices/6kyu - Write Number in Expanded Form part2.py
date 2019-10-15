"""
This is version 2 of my 'Write Number in Exanded Form' Kata.

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(1.24) # Should return '1 + 2/10 + 4/100'
expanded_form(7.304) # Should return '7 + 3/10 + 4/1000'
expanded_form(0.04) # Should return '4/100'

"""

def expanded_form(num):
    int_part,dec_part = str(num).split(".")
    l = []
    a = len(str(int_part))
    for i,j in enumerate(int_part):
        if j != '0':
            l.append(j+'0'*(a-i-1))
    for i,element in enumerate(dec_part):
        if element != '0':
            elem_new = element + "/1" + "0"*(i+1)
            l.append(elem_new)
    return " + ".join(l)

#sample:
def expanded_form(num):
    integer_part, fractional_part = str(num).split('.')

    result = [str(int(num) * (10 ** i)) for i, num in enumerate(integer_part[::-1]) if num != '0'][::-1]
    result += [str(num) + '/' + str(10 ** (i + 1)) for i, num in enumerate(fractional_part) if num != '0']

    return ' + '.join(result)


#enumerate(integer_part[::-1]) >> how to iterate numbers reversely

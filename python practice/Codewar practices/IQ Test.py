"""
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

"""

def iq_test(numbers):
    ns = [int(number) for number in numbers.split()]
    #making a string into an int list. "2 4 7 8 10" >>> [2,4,7,8,10]
    odd = 0
    even = 0
    index_odd = 0
    index_even = 0
    for i in range(len(ns)):
        if ns[i] % 2 == 0:
            even += 1
            index_even = i + 1
        else:
            odd += 1
            index_odd = i + 1

    if even > odd:
        return index_odd
    else:
        return index_even


# if i is going to be used for searching index, then range(len(x)) should be used

#sample rewriting:
def iq_test(numbers):
    number = [int(n) % 2 for n in numbers.split()]
    #making a string into an int list. "2 4 7 8 10" >>> [2,4,7,8,10]
    if number.count(0) > number.count(1):
    # if the number of occurance of 0 (i.e. even) is larger than that of 1 (i.e. odd)
        return number.index(1) + 1
    else:
        return number.index(0) + 1

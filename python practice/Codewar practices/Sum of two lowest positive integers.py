"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No floats or empty arrays will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.

"""

def sum_two_smallest_numbers(numbers):
    min_1 = min(numbers)
    numbers.remove(min_1)
    min_2 = min(numbers)
    return (min_1 + min_2)


#sample:

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

#use sorted first to make numbers in order, then find the sum of the first 2

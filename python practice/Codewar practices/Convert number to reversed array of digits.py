"""
Convert number to reversed array of digits
Given a random number:

C#: long;
C++: unsigned long;
You have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
"""

def digitize(n):
    digits = [int(x) for x in str(n)]
    digits.reverse()
    return digits


#sample1:
def digitize(n):
    return [int(x) for x in str(n)[::-1]]

#sample2:
def digitize(n):
  return [int(x) for x in reversed(str(n))]


#int object cannot be reversed

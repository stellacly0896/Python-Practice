"""
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""

def is_triangle(a, b, c):
  list = []
  list.append(a)
  list.append(b)
  list.append(c)
  list.sort()
  if ((list[0] + list[1]) > list[2]) and ((list[2] - list[1] < list[0])):
      return True
  return False


#sample:

def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

#simply make a list by using [a,b,c]

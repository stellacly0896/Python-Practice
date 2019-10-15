"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

def filter_list(l):
    lst = []
    for i in l:
        if type(i) == int:
            lst.append(i)
    return lst


#sample

def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]

"""
isinstance():

takes 2 parameters:
object - object to be checked
classinfo - class, type, or tuple of classes and types

The isinstance() returns:
True if the object is an instance or subclass of a class, or any element of the tuple
False otherwise
If classinfo is not a type or tuple of types, a TypeError exception is raised.

example:

class Foo:
  a = 5
fooInstance = Foo()

print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))

>True
>False
>True

"""

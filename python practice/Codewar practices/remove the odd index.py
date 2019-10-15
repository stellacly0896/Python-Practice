"""
 Write a Python program to remove the characters which have odd index values of a given string
 """

 def rmv_odd(str1):
     return str1[::2]

 print(rmv_odd("012345"))

 def rmv_odd(str1):
     str2 = ""
     for i in range(len(str1)):  # this is how you access the index of a string
         if i % 2 == 0:
             str2 += str1[i]
     return str2

 print(rmv_odd("012345"))

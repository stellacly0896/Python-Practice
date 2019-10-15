"""
 Write a Python program to find the second most repeated word in a given string.
 """

 def the_2nd(text):
    d = {}
    for word in text.split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    value = sorted(d.values(),reverse = True) #this is how you sort a dict based on the value
    #d.values() will return a list


    for k,v in d.items():
        if v == value[1]:
            return k,v
print(the_2nd("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))

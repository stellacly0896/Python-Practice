"""
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""

def poor(sent):
    loc_not = sent.find('not')
    loc_poor = sent.find('poor')

    if loc_poor > loc_not and loc_poor > 0 and loc_not >0:
        sent = sent.replace(sent[loc_not:(loc_poor + 4)],"good")
    return sent

sent1 = "The lyrics is poor!"
sent2 = "The lyrics is not that poor!"

print(poor(sent1),poor(sent2))


#.find() returns an index
# you can slice a string by s[loc_not : (loc_poor) + 4]

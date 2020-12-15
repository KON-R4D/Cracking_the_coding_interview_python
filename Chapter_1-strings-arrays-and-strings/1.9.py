'''
QUESTION:
StringRotation:Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one call to 
isSubString (e.g., "waterbottle" is a rotation of"erbottlewat").

SOLUTION:

'''
#assuming this is the isSubtring funtion
def isSubstring(str1,str2):
    return str2 in str1

####### OUR IMPLEMENTATION BEGINS HERE ##############

def isRotation(str1,str2):
    if len(str1)>0 and len(str1)==len(str2):
        longStr1 = str1+str1
        return isSubstring(longStr1,str2)


####### OUR IMPLEMENTATION ENDS HERE ##############

#Driver Code
string1 = "waterbottle"
string2 = "erbottlewat"

isRotation(string1,string2)

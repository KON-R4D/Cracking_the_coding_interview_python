'''
QUESTION:
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.

SOLUTION:
To be more precise, strings with even length (after removing all non-letter characters) must have all even
counts of characters. Strings of an odd length must have exactly one character with an odd count.
It's therefore sufficient to say that, to be a permutation ot a palindrome, a string can have no 
more than one character that is odd. 
'''

####### OUR IMPLEMENTATION 1(HASHTABLE) BEGINS HERE  ##############
from collections import defaultdict
def isPalindromePerm(string):
    dictValues = frequencyDictionary(string)
    return checkMaxOneOdd(dictValues)

def frequencyDictionary(string):
    dictionary = defaultdict() #create dictionary lambda:0
    for char_ in string:
        char = ordValue(char_) #convert character into ord value case insensitive
        if char==-1: #if not character, skip
            continue
            
        if dictionary.get(char,0)==0: #initiate count if not present
            dictionary[char]=1
        else:
            dictionary[char]+=1 #increase count if present
    #print(dictionary.values())
    return dictionary.values()
            
def ordValue(char): #returns ord value of character case insensitive and -1 for non alphabet

    if ord(char) >= ord('a') and ord(char) <= ord('z'):
        return ord(char)-ord('a')
    elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
        return ord(char)-ord('A')
    else:
        return -1
    
def checkMaxOneOdd(arr):
    oddPresent = False
    for item in arr:
        if item%2!=0:
            if oddPresent:
                return False
            oddPresent = True
        return True
                            

####### OUR IMPLEMENTATION 1 ENDS HERE ##############


#Driver Code

string ="Tact Cxoa"
print(isPalindromePerm(string))

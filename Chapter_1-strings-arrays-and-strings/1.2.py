'''
QUESTION:
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


SOLUTION 1: Sort the strings.
If two strings are permutations, then we know they have the same characters, 
but in different orders. There­ fore, sorting the strings will put the characters from two
permutations in the same order.
We just need to compare the sorted versions of the strings.
'''

####### OUR IMPLEMENTATION 1 BEGINS HERE ##############

def isPermutation1(string1_,string2_):
    if len(string1_)!=len(string2_):
        return False
    string1, string2 = sorted(string1_), sorted(string2_)
    return string1 == string2
####### OUR IMPLEMENTATION 1 ENDS HERE ##############


'''
SOLUTION 2: Check if the two strings have identical character counts.
We can also use the definition of a permutation-two words with the 
same character counts-to implement this algorithm. We simply iterate 
through this code, counting how many times each character appears. 
Then, afterwards, we compare the two arrays.
'''


####### OUR IMPLEMENTATION 2 BEGINS HERE ##############

def isPermutation2(string1,string2):
    if len(string1)!=len(string2):
        return False
    
    chars = [0]*128 # hold letter counts in array, could use a dictionary too
    
    for i in range(len(string1)): #add letter counts for string1
        chars[ord(string1[i])]+=1
    
    for i in range(len(string2)): # subtract letter counts from string2
        chars[ord(string2[i])]-=1
        if chars[ord(string2[i])] < 0: # this will capture all cases since we already ruled out diff length strings
            return false
        

####### OUR IMPLEMENTATION 2 ENDS HERE ##############

def isPermutation2(string1_,string2_):
    
    string1, string2 = sorted(string1_), sorted(string2_)
    return string1 == string2
####### OUR IMPLEMENTATION 2 ENDS HERE ##############


# Driver Code
string1 = "this is a string"
string2 = "is this a string"

print(isPermutation1(string1,string2))
print(isPermutation2(string1,string2))
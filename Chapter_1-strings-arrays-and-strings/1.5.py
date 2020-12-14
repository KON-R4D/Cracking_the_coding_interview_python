'''
QUESTION:
One Away: There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. 
Given two strings, write a function to check if 
they are one edit (or zero edits) away.


SOLUTION:
Use a hashtable to keep track of letter counts and check for if more than 2 letters have odd counts

'''

####### OUR IMPLEMENTATION 1 BEGINS HERE ##############
from collections import defaultdict

def isOneAway(str_1,str_2):
    oddCount=0 #counter number odd count
    dict_ = defaultdict() 
    
    ## populate the dictionary
    for item in str_1:
        if(dict_.get(item,0)==0):
            dict_[item]=1
        else:
            dict_[item]+=1
    for item in str_2:
        if(dict_.get(item,0)==0):
            dict_[item]=1
        else:
            dict_[item]+=1
    ## check for odd counts
    for item in dict_.values():
        if item%2==1:
            oddCount+=1
            if oddCount>2:
                return False
    return True
    
    
    
####### OUR IMPLEMENTATION 1 ENDS HERE ##############

#Driver Code
print("pale, ple -> True. Code says:",isOneAway('pale','ple'))
print("pales, pale -> True. Code says:",isOneAway('pale','pale'))
print("pale, bale -> True. Code says:",isOneAway('pale','bale'))
print("pale, bae -> False. Code says:",isOneAway('pale','bae'))

'''
QUESTION:
Is Unique: Implement an algorithm to determine if a string 
has all unique characters. What if you cannot use additional data structures?


SOLUTION:
One solution is to create an array of boolean values, where the flag at index i 
indicates whether character i in the alphabet is contained in the string.
The second time you see this character you can immediately return false.
We can also immediately return false if the string length exceeds the number of unique 
characters in the alphabet. After all, you can't form a string of 280 unique characters 
out of a 128-character alphabet.
'''

####### OUR IMPLEMENTATION 1 GOES HERE ##############

def isUnique1(string):
    
    #check if length of string is greater than our alphabet
    if len(string)>128:
        return False
    
    #create an exists array of size of our alphabet
    exists = [False]*128
    
    #loop through string and mark as exists character ,checking for its existence at each step
    for i in range(len(string)):
        if exists[ord(string[i])]:
            return False
        exists[ord(string[i])]=True
    return True
    
    
####### OUR IMPLEMENTATION 1 ENDS HERE ##############




'''
SOLUTION 2:

We can reduce our space usage by a factor of eight by using a bit vector. 
We will assume, in the below code, that the string only 
uses the lowercase letters a through z. This will allow us to use just a single int.

Link to a good explanation of the method seen in the book
https://stackoverflow.com/questions/25847191/new-to-java-trying-to-understand-checker-1-val

Link to python bitwise operators
https://wiki.python.org/moin/BitwiseOperators
'''


####### OUR IMPLEMENTATION 2 GOES HERE ##############

def isUnique2(string):
    
    #set checker to 0
    checker =0
    for i in range(len(string)):
        #shift value by getting distance from a
        val = ord(string[i])- ord('a')
        
        # & Does a "bitwise and". Each bit of the output is 1 if the corresponding 
        #bit of x AND of y is 1, otherwise it's 0. e.g
        
        #check = 0000 0000 0000 0000 0000 1000 1000 0010   &  
        #'b'   = 0000 0000 0000 0000 0000 0000 0000 0010 
       #    ----------------------------------------------
       #result= 0000 0000 0000 0000 0000 0000 0000 0010
        
        if checker & (1<<val) > 0:
            return False
        
        # | Does a "bitwise or". Each bit of the output is 0 if the corresponding 
        # bit of x AND of y is 0, otherwise it's 1.
        
        checker |=(1<<val)
    return True
    
    
####### OUR IMPLEMENTATION 2 ENDS HERE ##############

#Driver Code
string = "abdc"
isUnique1(string)#true

string = "abdcd"
isUnique2(string)#false
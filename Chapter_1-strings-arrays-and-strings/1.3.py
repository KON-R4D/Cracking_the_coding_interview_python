'''
QUESTION:
URLify: Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the end to hold 
the additional characters, and that you are given the "true" length of the string.


SOLUTION 1:
If allowed to use inbuilt split function in python

'''


####### OUR IMPLEMENTATION 1 BEGINS HERE ##############
def URLify1(string):
    str_arr = string.split() # split the string by spaces
    url=""
    
    for string in str_arr: #join the different segments by appending "%20": we have to remone the extra one at the end
        url+=string+"%20"
    
    return url[:-3]
    
####### OUR IMPLEMENTATION 1 ENDS HERE ##############


#Driver code
string = "this string has a couple of spaces"
URLify(string)

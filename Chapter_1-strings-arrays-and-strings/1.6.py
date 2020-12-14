'''
QUESTION:
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. 
If the "compressed" string would not become smaller than the original string, 
your method should return the original string. You can assume the string has 
only uppercase and lowercase letters (a - z).

SOLUTION:

'''

####### OUR IMPLEMENTATION 1 BEGINS HERE ##############


def compress(string):
    compressed = [] #create array to hold results
    countConsecutive=0 
    for i in range(len(string)):
        countConsecutive+=1 #increment counter by 1
        
        #if next is different from current, then append this to result (or if we are at the end of the string)
        if (i+1) >= len(string) or string[i]!=string[i+1]:
            compressed.append(string[i])
            compressed.append(str(countConsecutive)) #ensure to add digits as type strings to array
            countConsecutive = 0
            
        
    return "".join(compressed) #return array as string

####### OUR IMPLEMENTATION 1 ENDS HERE ##############




#Driver Code
string = 'aabcccccaaa'
compress(string)

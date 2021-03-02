# create the Trie node to capture state(if it is the last node), as well as references to nodes after 
# this trie will only work for lowercase letters

class TrieNode:
    def __init__(self):
        
        #create a node and reference to children nodes
        self.children = [None]*26
        
        # indicate if it is the end of a word
        self.isEndOfWord = False
        
        
class Trie(TrieNode):
    def __init__(self):
        
        # create a root holding references to all letters of the English Alphabet
        self.root = TrieNode()
    
    def indexOfInterest(self,char):
        
        # return the index equivalent of the character from a so that we can use this as position in array
        return ord(char)-ord('a')
    
    def insert(self,elems):
        
        # obtain number of elements to insert
        size = len(elems)
        level_of_trie_to_check = self.root
        
        for position in range(size):
            # for each letter in elements to insert
            # check from root for letter and only add child if it does not exist down the line
            
            char_of_interest = elems[position] #extract character
            index = self.indexOfInterest(char_of_interest) # extract index of character
            
            if not level_of_trie_to_check.children[index]: # if does not exist, add it at this location
                level_of_trie_to_check.children[index] = TrieNode()
            
            level_of_trie_to_check = level_of_trie_to_check.children[index]
        
        level_of_trie_to_check.isEndOfWord = True
        
    def search(self,elems):
        
        # obtain size of word to search
        size = len(elems)
        level_of_trie_to_check = self.root
        
        for position in range(size):
            
            char_of_interest = elems[position]
            index = self.indexOfInterest(char_of_interest)
            
            if not level_of_trie_to_check.children[index]: # if sequence breaks, then word does not exist
                return False
            
            level_of_trie_to_check = level_of_trie_to_check.children[index]
            
        return level_of_trie_to_check.isEndOfWord == True


# Driver code
sample = Trie()

sample.insert('bible')
sample.insert('bottle')
sample.insert('bag')
sample.insert('true')
sample.insert('false')


sample.search('bottle')
sample.search('bag')
sample.search('true')
sample.search('man')

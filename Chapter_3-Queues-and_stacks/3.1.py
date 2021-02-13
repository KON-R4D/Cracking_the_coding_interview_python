'''
QUESTION:

Three in One: 
Describe how you could use a single array to implement three stacks.

SOLUTION:
we can have it such that each stack has a range of indexes within the stack left out for it
alternatively we can have it such that each stack the next item is in position index+3
'''

######### our implementation starts here ########### 

class three_for_one_stack():
    
    def __init__(self):
        self.stack = [False]*100 # array of capicity 100
        self.last_altered_index=[False,False,False] # store last altered index for each stack
        self.last_remove_index=[0,1,2] # store last removed index for each stack
        
    def add_to_stack(self,stack_number,item): 
        if self.last_altered_index[stack_number-1]==False: # if last altered index is False
            if stack_number==1: # for stack 1, first index is 0
                self.stack[0]=item
                self.last_altered_index[stack_number-1]=0 
            elif stack_number ==2: # first index for stack 2 is 1
                self.stack[1]=item
                self.last_altered_index[stack_number-1]=1
            elif stack_number==3: # first index for stack 2 is 2
                self.stack[2]=item
                self.last_altered_index[stack_number-1]=2
        else: # if last altered index has an index
            new_index = self.last_altered_index[stack_number-1]+3 # calculate the new index for the given stack
            self.stack[new_index]=item # place item in the new index
            self.last_altered_index[stack_number-1]=new_index # update last altered index for the given stack
    
    def pop_from_stack(self,stack_number):
        index = self.last_remove_index[stack_number-1] # get index of the last removed item from stack
        if index+1>len(self.stack): # if index greater than capacity, return 
            return
        data = self.stack[index] # otherwise get the value in the given index
        self.stack[index]=False # mark content in index as false
        self.last_remove_index[stack_number-1]=index+3 # update last remove index
        return data # return the data 

######### our implementation ends here ########### 


# Driver code
s = three_for_one_stack()
s.add_to_stack(2,5) # add 5 to stack 2
s.add_to_stack(2,3) # add 3 to stack 2
s.add_to_stack(2,4) # add 4 to stack 2

s.add_to_stack(1,3) # add 3 to stack 1
s.add_to_stack(1,4) # add 4 to stack 1

s.add_to_stack(3,3) # add 3 to stack 3
s.add_to_stack(3,4) # add 4 to stack 3

s.stack
s.pop_from_stack(2)
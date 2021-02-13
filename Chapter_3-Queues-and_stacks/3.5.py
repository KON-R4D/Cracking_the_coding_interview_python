'''
QUESTION:
Sort Stack: 
Write a program to sort a stack such that 
the smallest items are on the top. You can use an additional temporary stack, 
but you may not copy the elements into any other data structure 
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.


SOLUTION:
2 Stacks, 1 with sorted elements; the other to help with the sorting. If new item is less than top item in 
sorted, add to top of sorted. Otherwise, move all values less than to sorting stack, push item to sorted,
the push back all the other items from sorted.

'''


######### our implementation starts here ###########

def sort_stack(stack):
    sorting_stack = stack
    sorted_stack = MyStack()
    
    next_item = sorting_stack.pop()
    while(next_item):
        #print(sorted_stack.peek())
        
        if sorted_stack.peek()==False:
            
            sorted_stack.push(next_item)
            next_item = sorting_stack.pop()
            
            continue
        if next_item < sorted_stack.peek():
            sorted_stack.push(next_item)
        else:
            #move everything less than next_item to the sorting stack
            next_sorted_item = sorted_stack.peek()
            while next_sorted_item !=False and next_item>next_sorted_item:
                sorting_stack.push(sorted_stack.pop())
                next_sorted_item = sorted_stack.peek()
            sorted_stack.push(next_item)
                
        
        next_item = sorting_stack.pop()
    return sorted_stack

######### our implementation ends here ###########

# Driver code

s= MyStack()
s.push(1)
s.push(7)
s.push(5)
s.push(6)
s.push(4)

p = sort_stack(s)
p.pop()
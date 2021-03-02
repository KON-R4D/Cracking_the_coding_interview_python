'''
# min-heap with insert and extract min functionalities
# left child index: (index*2) + 1
# right child index: (index*2) +2
# parent index: (index-1)//2

# to convert a minheap taking in digits to a maxheap, we can just multiply by -1 before inserting then by -1
# after extracting

'''

class MinHeap:
    
    def __init__(self):
        self.min_heap = []
        
    def show(self):
        return self.min_heap
        
    def insert(self,elem):
        #insert element to last index then bubble up swapping parent and elem if parent > elem
        self.min_heap.append(elem)
        
        #bubble up
        self.bubble_up()
    
    def extract_min(self):
        if len(self.min_heap)==0:
            return
        
        #extract the min element from the top of the list
        min_elem = self.min_heap[0]
        
        #swap the top elem with the last elem 
        last_index = len(self.min_heap)-1
        self.min_heap[0],self.min_heap[last_index]=self.min_heap[last_index],self.min_heap[0]
        
        #delete the last element 
        del self.min_heap[last_index]
        
        #bubble down 
        self.bubble_down()
        
        #return minimum element 
        return min_elem
        
        
    
    
    def bubble_up(self):
        last_index = len(self.min_heap)-1
        parent = (last_index-1)//2
        
        while last_index >= 0 and parent >= 0 and self.min_heap[last_index] < self.min_heap[parent]:
            
            #swap parent for last index since the condition is catered for in the while loop
            self.min_heap[parent],self.min_heap[last_index]=self.min_heap[last_index],self.min_heap[parent]
            
            last_index = parent 
            parent = (last_index-1)//2
        
    
    def bubble_down(self):
        top_index = 0
        last_index = len(self.min_heap)-1
        left_child = (top_index*2)+1
        right_child = (top_index*2)+2
        
        while (top_index <= last_index and right_child <=last_index) and (self.min_heap[top_index]>self.min_heap[left_child]
             or self.min_heap[top_index]> self.min_heap[right_child]):
            
            
            if self.min_heap[right_child]<self.min_heap[left_child]:
                
                #if right child is less than left child, swap with right child
                self.min_heap[top_index],self.min_heap[right_child]=self.min_heap[right_child],self.min_heap[top_index]
                
                #make right_child new top item
                top_index = right_child
            else:
                self.min_heap[top_index],self.min_heap[left_child]=self.min_heap[left_child],self.min_heap[top_index]
                
                #make left_child new top item
                top_index = left_child
                
                
            left_child = (top_index*2)+1
            right_child = (top_index*2)+2


# Driver code

min_heap = MinHeap()
min_heap.insert(4)
min_heap.insert(50)
min_heap.insert(7)
min_heap.insert(55)
min_heap.insert(90)
min_heap.insert(87)
min_heap.insert(2)

min_heap.show()

min_heap.extract_min()

min_heap.show()

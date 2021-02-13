
'''
QUESTION:
Animal Shelter: 
An animal shelter, which holds only dogs and cats, operates
on a strictly "first in, first out" basis. People must adopt either the"oldest"
(based on arrival time) of all animals at the shelter, or they can select whether
they would prefer a dog or a cat (and will receive the oldest animal of that type). 
They cannot select which specific animal they would like. Create the data structures to 
maintain this system and implement operations such as enqueue, 
dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list data structure.


SOLUTION:
Can implement a linkedlist that will have the features of a queue. to deque any animal, the top most
node of the queue will be popped out. To deque a partical animal, find the first occurance of that animal
then adjust the linked list appropriately

'''
######### our implementation starts here ###########

from collections import deque
class AnimalNode():
    def __init__(self,name,type):
        self.name = name
        self.type = type
        #self.next = None

        
class AnimalShelter(AnimalNode):
    def __init__(self):
        self.queue=deque()
    
    def enqueue(self,name,type):
        new_animal = AnimalNode(name,type)
        
        self.queue.append(new_animal)
    
    def dequeueAny(self):
        if len(self.queue)==0:
            return
        return self.queue.popleft().name
    
    def dequeueDog(self):
        for animal in self.queue:
            if animal.type == "dog":
                #index = self.queue.index(animal)
                target = animal
                self.queue.remove(target)
                return target.name
                #return self.queue.pop(index).name
        return
    
    def dequeueCat(self):
        for animal in self.queue:
            if animal.type == "cat":
                target = animal
                self.queue.remove(target)
                return target.name
        return

######### our implementation ends here ###########



'''

SOLUTION 2:
Use two linked lists and pop out the top element for cat or dog, then compare lesser counter for any
'''


######### our implementation starts here ###########


from collections import deque
class AnimalNode2():
    def __init__(self,name,type,count):
        self.name = name
        self.type = type
        self.count = count

        
class AnimalShelter2(AnimalNode2):
    def __init__(self):
        self.queue_cat=deque()
        self.queue_dog = deque()
        self.count = 0
    
    def enqueue(self,name,type):
        new_animal = AnimalNode2(name,type,self.count)
        self.count+=1
        
        
        if type == "cat":
            self.queue_cat.append(new_animal)
        else:
            self.queue_dog.append(new_animal)
            
        
        
    
    def dequeueAny(self):
        if len(self.queue_cat)==0:
            return self.dequeueDog()
        elif len(self.queue_dog)==0:
            return self.dequeueCat()
        if self.queue_dog[0].count < self.queue_cat[0].count:
            return self.dequeueDog()
        else:
            return self.dequeueCat()
            
        
    
    def dequeueDog(self):
        if len(self.queue_dog)==0:
            return
        return self.queue_dog.popleft().name
    
    def dequeueCat(self):
        if len(self.queue_cat)==0:
            return
        return self.queue_cat.popleft().name
######### our implementation ends here ###########




# Driver code

AS= AnimalShelter2()
AS.enqueue('Thomas','cat')
AS.enqueue('Brad','dog')
AS.enqueue('Scooby','dog')
AS.enqueue('Jerry','cat')
AS.enqueue('didi','cat')
AS.enqueue('Rexy','dog')
AS.enqueue('Lillt','cat')

AS.dequeueAny()
AS.dequeueCat()
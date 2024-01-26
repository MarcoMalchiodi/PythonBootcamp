class Node:
    def __init__(self,data=None):
        
        self.data = data
        self.next = None # the last element always has its last pointer set to none
        
        

class LinkedList:
        def __init__(self,data=None):
            
            self.head = Node() # the head node never contrains ay acrual data
        
        def append(self,data):
            new_node = Node(data)
            cur = self.head
            
            while cur.next != None:
                cur = cur.next # traversing to the next node
            # Once we know we are at the last element of the list:
            cur.next = new_node
        
        def length(self):
            cur = self.head
            total = 0 # num of nodes
            
            while cur.next != None:
                total +=1
                cur = cur.next 
            
            return total
        
        def display(self): # helper function to display the current content of our list
            elements = []
            cur_node = self.head
            
            while cur_node.next != None:
                cur_node = cur_node.next
                elements.append(cur_node.data)
            print(elements)
            
        def get(self,index):
            if index >= self.length():
                print("ERROR: index out of range")
                return None

            cur_index = 0
            cur_node = self.head
            
            while True:
                cur_node = cur_node.next
                
                if cur_index == index:
                    return cur_node.data
                cur_index += 1
                
        def erase(self,index):
            if index >= self.length():
                print("ERROR: index out of range")
                return None

            cur_index = 0
            cur_node = self.head
            
            while cur_node.next is not None:
                last_node = cur_node
                cur_node = cur_node.next
                
                if cur_index == index:
                    last_node.next = cur_node.next
                    return(cur_index)
                cur_index += 1
            
            
my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print("Element at 2nd index: ", my_list.get(2))
print("____________________________________________________")

my_list.erase(1)
my_list.display()
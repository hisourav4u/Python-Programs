class Node:

	def __init__(self, name, age, salary):
		## data of the node
		self.name = name
		self.age = age
		self.salary = salary

		## next pointer
		self.next = None

class LinkedList:

    def __init__(self):
		## initializing the head with None
		self.head = None

	def insert(self, new_node):
		## check whether the head is empty or not
		if self.head:
			## getting the last node
			last_node = self.head
			while last_node.next != None:
				last_node = last_node.next

			## assigning the new node to the next pointer of last node
			last_node.next = new_node

		else:
			## head is empty
			## assigning the node to head
			self.head = new_node
			
	def display(self):
		## variable for list iteration
		temp_node = self.head

		## iterating until we reach the end of the linked list
		while temp_node != None:
			## printing the node data
			print(temp_node.data, end='->')

			## moving to the next node
			temp_node = temp_node.next

		print('Null')

    def getMiddle(self, head):
        if head == None: 
            return head
        else:
            # Tortoise and Hare Algorithms
            slow = fast = head
            while(fast.next != None and fast.next.next != None):
                slow = slow.next
                fast = fast.next.next
            return slow                 ## Middle Node;        
    
    
    def merge(self,left,right):
        head = None
         
        # Base cases
        if left == None:
            return right
        if right == None:
            return left
             
        if left.name < right.name:
            head = left
            head.next = self.merge(left.next, right)
        else:
            head = right
            head.next = self.merge(left, right.next)
            
        return head
    
    
    def mergeSort(self, head):
        if head == None or head.next == None:
            return head
        else:
            midNode = self.getMiddle(head)                ## Mid Node
            nextMidNode = midNode.next                    ## Node From, NextMidNode -> End
            midNode.next = None                           ## Node From, Head -> MidNode
            
            left = self.mergeSort(head)                   ## Left Linked List;
            right = self.mergeSort(nextMidNode)           ## Rigth Linked List;
            
            return self.merge(left, right)
    
    
    def sortList():
        if self.head == None or self.head.next == None:
            return self.head
        return self.mergeSort(self.head)
    
    
if __name__ == '__main__':
	## instantiating the linked list
	linked_list = LinkedList()
    
    ##taking input for 10 people
    for i in range(10):
        name=input("Enter the name: ")
        age=input("Enter the age: ")
        salary=input("Enter the salary: ")
        
        ##inserting the input data to the linked list
        linked_list.insert(Node(name, age, salary))
    
    ##sorting the linked list   
    linked_list.sortList()
    
    ##Printing the result
    linked_list.display()
    
    
    

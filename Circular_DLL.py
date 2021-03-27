"""
Circular doubly linked list doesn't contain NULL in any of the node. 
The last node of the list contains the address of the first node of the list. 
The first node of the list also contain address of the last node in its previous pointer
"""

class Node():
	def __init__(self, data1):
		self.data = data1
		self.next = None
		self.prev = None

class LinkedList():
	def __init__(self):
		self.head = None
		self.tail = None

	def insertAtStart(self, data2):
		self.new_node = Node(data2)

		if not self.head:
			self.head = self.new_node 
			self.tail = self.new_node
			self.new_node.next = self.head
			self.new_node.prev = self.head

		else:
			self.head.prev = self.new_node
			self.new_node.next = self.head
			self.new_node.prev = self.head.prev
			self.tail.next = self.new_node
			self.head = self.new_node

	def insertAtEnd(self, data2):
		self.new_node = Node(data2)

		if not self.head:
			self.head = self.new_node 
			self.tail = self.new_node
			self.new_node.next = self.head
			self.new_node.prev = self.head

		else:
			self.tail.next = self.new_node
			self.new_node.prev = self.tail
			self.new_node.next = self.head
			self.head.prev = self.new_node
			self.tail = self.new_node

	def removeFromStart(self):
		self.second_element = self.head.next
		self.last_element = self.tail

		self.last_element.next = self.second_element
		self.second_element.prev = self.last_element
		self.head.next = None
		self.head.prev = None
		self.head = self.second_element

	def removeFromEnd(self):
		self.secondlast_element = self.tail.prev
		self.first_element = self.head

		self.secondlast_element.next = self.first_element
		self.first_element.prev = self.secondlast_element
		self.tail.next = None
		self.tail.prev = None
		self.tail = self.secondlast_element

	def printLL(self):
		self.temp = self.head
		elements = []
		while(True):
			elements.append(str(self.temp.data))
			self.temp = self.temp.next
			if(self.temp == self.head):
				break
		print(" --> ".join(elements))

l1 = LinkedList()
l1.insertAtEnd("Amazon")
l1.insertAtEnd("Apple")
l1.insertAtEnd("Netflix")
l1.insertAtEnd("Google")
l1.insertAtEnd("Twitter")
l1.insertAtEnd("Reddit")
l1.insertAtStart("Facebook")
print("Original Linked List : ")
l1.printLL()
print("Element removed from first : ")
l1.removeFromStart()
l1.printLL()
print("Element removed from last : ")
l1.removeFromEnd()
l1.printLL()
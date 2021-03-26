"""
Reverse a Linked List by using just one pass
Without using Previous variable
"""

class Node():
	def __init__(self, data1):
		self.data = data1
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None

	def push(self, data2):
		new_node = Node(data2)

		if not self.head:
			self.head = new_node
		else:
			self.temp = self.head
			while(self.temp.next is not None):
				self.temp = self.temp.next
			self.temp.next = new_node

	def printLL(self):
		self.temp = self.head
		while (self.temp is not None):
			print(self.temp.data)
			self.temp = self.temp.next

	def reverse(self):
		if((self.head is None) or (self.head.next is None)):
			return self.head

		else:
			self.curr_element = self.head
			self.next_element = self.head.next

			while(self.next_element is not None):
				self.temp = self.next_element
				self.temp.next = self.curr_element
				self.next_element = self.next_element.next
				self.curr_element = self.temp

			return self.curr_element

l1 = LinkedList()
l1.push(10)
l1.push(20)
l1.push(30)
l1.push(40)
l1.push(50)
print("Original Linked List : ")
l1.printLL()
l1.head = l1.reverse()
print("Reversed Linked List : ")
l1.printLL()
"""
Define a Linked List and perform the operations in a FIFO (First-In-First-Out) format
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

	def remove(self):
		if not self.head:
			print("No element to remove")
		else:
			self.head = self.head.next
			print("Element is removed")

	def printLL(self):
		self.temp = self.head
		elements = []
		while(self.temp is not None):
			elements.append(str(self.temp.data))
			self.temp = self.temp.next
		print(" ---> ".join(elements))

l1 = LinkedList()
l1.push(13)
l1.push(26)
l1.push(39)
l1.push(52)
l1.push(65)
print("Original LinkedList : ")
l1.printLL()
l1.remove()
print("After Removal : ")
l1.printLL()
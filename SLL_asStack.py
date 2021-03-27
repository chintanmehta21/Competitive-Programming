"""
Implementing the push and pop operations of Stack (LIFO - Last In First Out)
in LinkedLists
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
		if not self.head:
			print("No elements in the Linked List")

		else:
			self.temp = self.head
			elements = []
			while(self.temp is not None):
				elements.append(self.temp.data)
				self.temp = self.temp.next
			print(" --> ".join(elements))

	def remove(self):
		self.prev = self.head
		self.current = self.head.next

		while(self.current.next is not None):
			self.prev = self.current
			self.current = self.current.next

		self.prev.next = None
		print("Element removed")


l1 = LinkedList()
l1.push("Python")
l1.push("Java")
l1.push("C++")
l1.push("C#")
l1.push("Machine Learning")
print("Original Linked List : ")
l1.printLL()
l1.remove()
print("Removed Linked List : ")
l1.printLL()
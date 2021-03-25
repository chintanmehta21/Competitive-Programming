"""
Two changes from the last program of Reversing a Linked List : 
1. Storing the Linked List in a linear form one after the other in the order it is input
2. Reversing the Linked List using Recursion instead of Iteration
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

	def reverseLL(self, item, l1):
		
		if item.next is None:
			print(item.data)
			self.temp.next = None
			if self.temp != self.head:
				l1.reverseLL(l1.head, l1)
			else:
				print(self.temp.data)
		else:
			self.temp = item
			l1.reverseLL(item.next, l1)

	def printList(self):
		self.temp = self.head
		while(self.temp is not None):
			print(self.temp.data)
			self.temp = self.temp.next

l1 = LinkedList()
l1.push(1)
l1.push(2)
l1.push(3)
l1.push(4)
l1.push(5)
print("Original List : ")
l1.printList()
print("Reversed List : ")
l1.reverseLL(l1.head, l1)

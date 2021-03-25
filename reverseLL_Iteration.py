"""
Intitialize a Linked List and reverse the same
"""

class Node:
	def __init__(self, data1):
		self.data = data1
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data2):
		new_node = Node(data2)
		new_node.next = self.head
		self.head = new_node

	def reverse(self):
		current = self.head
		prev = None
		while(current != None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

	def print(self):
		temp = self.head
		while(temp is not None):
			print(" ", temp.data)
			temp = temp.next


list1 = LinkedList()
list1.push(8)
list1.push(11)
list1.push(10)
list1.push(9)
list1.push(7)
print("Original LinkedList : ")
list1.print()
list1.reverse()
print("Reversed LinkedList : ")
list1.print()

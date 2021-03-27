"""
Circular linked list is a linked list where all nodes are connected to form a circle
There is no NULL at the end
"""

class Node():
	def __init__(self, data1):
		self.data = data1
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None

	def push(self, data2):
		self.new_node = Node(data2)

		if not self.head:
			self.head = self.new_node
			self.new_node.next = self.head

		else:
			self.temp = self.head
			while(self.temp.next != self.head):
				self.temp = self.temp.next

			self.temp.next = self.new_node
			self.new_node.next = self.head

	def remove(self):
		self.prev = self.head
		self.curr = self.head.next

		while(self.curr.next != self.head):
			self.prev = self.curr
			self.curr = self.curr.next

		self.prev.next = self.head
		self.curr.next = None

	def printLL(self):
		if not self.head:
			print("Empty Linked List")

		else:
			elements = []
			self.temp = self.head
			while(1):
				elements.append(str(self.temp.data))
				self.temp = self.temp.next
				if(self.temp == self.head):
					break
			print(" --> ".join(elements))

l1 = LinkedList()
l1.push(20)
l1.push(40)
l1.push(60)
l1.push(80)
l1.push(100)
print("Original Linked List : ")
l1.printLL()
l1.remove()
print("Removed element Linked List : ")
l1.printLL()
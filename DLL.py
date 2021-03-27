"""
Doubly Linked List program
Here, we can insert or remove elements from both ends in O(1) complexity
Here, pos stands for position ("S" is Start and "E" is End)
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

	def push(self, data2, pos="E"):
		self.new_node = Node(data2)
		if not self.head:
				self.head = self.new_node
				self.tail = self.new_node

		else:
			if pos == "E":
				self.temp = self.head
				while(self.temp.next is not None):
					self.temp = self.temp.next

				self.new_node.prev = self.temp
				self.temp.next = self.new_node
				self.tail = self.new_node

			elif pos == "S":
				self.temp = self.head
				self.temp.prev = self.new_node
				self.new_node.next = self.temp
				self.head = self.new_node

			else:
				print("Incorrect Position")

	def remove(self, pos = "E"):
		if not self.head:
			print("Empty Linked List")

		else:
			if pos == "S":
				self.temp = self.head.next
				self.temp.prev = None
				self.head.next = None
				self.head = self.temp

			elif pos == "E":
				self.temp = self.tail.prev
				self.temp.next = None
				self.tail.prev = None
				self.tail = self.temp

			else:
				print("Incorrect Position")

	def printLL(self, pos = "S"):
		if not self.head:
			print("Empty Linked List")

		else:
			if pos == "S":
				elements = []
				self.temp = self.head
				while(self.temp):
					elements.append(str(self.temp.data))
					self.temp = self.temp.next
				print(" --> ".join(elements))

			elif pos == "E":
				elements = []
				self.temp = self.tail
				while(self.temp):
					elements.append(str(self.temp.data))
					self.temp = self.temp.prev
				print(" --> ".join(elements))

l1 = LinkedList()
l1.push(5)
l1.push(10)
l1.push(15)
l1.push(20)
l1.push(25)
l1.push(30)
l1.push(35)
l1.push(40)
l1.push(45)
l1.push(50)
l1.push(55)
print("Original Linked List : ")
l1.printLL()
print("Element removed from Start : ")
l1.remove("S")
l1.printLL()
print("Element removed from End : ")
l1.remove("E")
l1.printLL()
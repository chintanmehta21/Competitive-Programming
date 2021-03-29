"""
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) manner
"""

class Stack():
	def __init__(self):
		self.elements = []
		self.count = 0

	def push(self, data):
		self.elements.append(data)
		self.count += 1

	def pop(self):
		self.elements.pop()
		self.count -= 1

	def peek(self):
		return self.elements[-1]

	def is_empty(self):
		if len(self.elements) == 0:
			return True
		else:
			return False

	def printStack(self):
		for i in reversed(self.elements):
			print(i)

s1 = Stack()
s1.push(10)
s1.push(15)
s1.push(20)
s1.push(25)
s1.push(30)
s1.push(35)
print("Current Stack : ")
s1.printStack()
print("Popping one element : ")
s1.pop()
print("Current Stack : ")
s1.printStack()
print("Top element : ", s1.peek())
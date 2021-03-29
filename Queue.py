"""
Queue is a linear data structure that stores items in First In First Out (FIFO) manner
Insertion happens only at one end called the rear end ==> [Enqueue]
Deletion happens only at one end called the front end ==> [Dequeue]
"""

class Queue():
	def __init__(self):
		self.size = 5
		#ideally size = int(input("Enter the size of the queue"))
		self.queue = [None] * self.size
		self.rear = -1
		self.front = 0
		self.count = 0

	def isFull(self):
		if(self.count == self.size):
			return True
		else:
			return False

	def isEmpty(self):
		if(self.count == 0):
			return True
		else:
			return False

	def EnQueue(self, data):
		if(self.isFull()):
			print("Queue is full")
		else:
			self.rear = (self.rear + 1) % self.size
			self.queue[self.rear] = data
			self.count += 1

	def DeQueue(self):
		if(self.isEmpty()):
			print("Queue is empty")
		else:
			print("DeQueued element is ", self.queue[self.front])
			self.queue[self.front] = None
			self.front = (self.front + 1) % self.size
			self.count -= 1

	def printQueue(self):
		if(self.isEmpty()):
			print("Queue is empty")
		else:
			for i in range(self.size):
				print(self.queue[int((self.front + i) % self.size)], end = " --> ")

q1 = Queue()
q1.EnQueue(10)
q1.EnQueue(20)
q1.EnQueue(30)
q1.EnQueue(40)
print("Current Queue : ")
q1.printQueue()
print("DeQueueing one element...")
q1.DeQueue()
print("Current Queue : ")
q1.printQueue()
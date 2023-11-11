class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue:
	def __init__(self)
		self.head = None 
		self.tail = None 

	def enqueue(self, data):
		new_node = Node()

		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
	def dequeue(self):
		if self.head:
			current = self.head
			self.head = current.next
			current.next = None

			if self.head is None:
				self.tail = None
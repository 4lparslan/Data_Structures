class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert_at_beginning(self, data):
		new_node = Node(data)

		if self.head:
			new_node.next = self.head
			self.head = new_node
		else:
			self.head = new_node
			self.tail = new_node
	def remove_at_beginning(self):
		if self.head:
			if self.head == self.tail:
				self.head = None
				self.tail = None 
			else:
				self.head = self.head.next
		else:
			print("Linked List is empty.")

	def insert_at_end(self,data):
		new_node = Node(data)

		if self.head:
			self.tail.next = new_node
			self.tail = new_node
		else:
			self.head = new_node
			self.tail = new_node
	def remove_at_end(self):
		if self.tail:
			if self.head == self.tail:
				self.head = None
				self.tail = None 
			else:
				current = self.head

				while current.next != self.tail:
					current = current.next
				current.next = None
				self.tail = current
		else:
			print("Linked List is empty.")
	def insert_at(self, data, position):
		new_node = Node(data)
		if position == 0:
			self.insert_at_beginning(data)
			return
		current = self.head
		index = 0
		while current:
			if index == position - 1:
				new_node.next = current.next
				current.next = new_node
				if current == self.tail:
					self.tail = new_node
				return
			current = current.next
			index += 1
	def remove_at(self, position):
		if self.head is None:
			print("Linked List is empty.")
		if position == 0:
			self.remove_at_beginning(data)
			return
		current = self.head
		index = 0
		while current:
			if index == position - 1:
				if current.next == self.tail:
					self.tail = current
				current.next = current.next.next
				return
			current = current.next
			index+=1
	def search(self, data):
		current = self.head

		while current:
			if current.data == data:
				return True
			else:
				current = current.next
		return False
	def display(self):
		if self.head:
			current = self.head

			while current:
				print(current.data, end=" -> ")
				current = current.next
			print("")
		else:
			print("Linked List is empty.")


deneme = LinkedList()
deneme.insert_at_end("SUSI")
deneme.insert_at_end("DONER")
deneme.insert_at_beginning("KEBAB")

deneme.display()
print(deneme.search("defdf"))
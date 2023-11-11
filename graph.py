class Graph:
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, vertex):
		self.vertices[vertex] = []

	def add_edge(self, source, target):
		self.vertices[source].append(target)

my_graph = Graph()

my_graph.add_vertex("David")
my_graph.add_vertex("Jack")
my_graph.add_vertex("Ali")

my_graph.add_edge("David", "Jack")
my_graph.add_edge("David", "Ali")
my_graph.add_edge("Jack", "Ali")

print(my_graph.vertices)
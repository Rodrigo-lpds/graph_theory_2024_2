class Graph:
	def __init__(self, file_name):
		self.file_name = file_name
		self.readed_graph = self.read_graph_file()
		self.vertices_quantity = self.vertices_qty() + 1
		self.edges = self.edges_array()

	def read_graph_file(self):
		"""
		Reads a graph file and returns a list of all the lines in the file.
		"""
		with open(self.file_name, 'r') as file:
			return file.read().splitlines()
    
	def vertices_qty(self):
			"""
			Returns the vertices quantity of the graph.
			"""
			return int(self.readed_graph[0].rstrip("\n"))
	
	def edges_array(self): # use graph representation instead
		"""
		Returns a matriz with all edges of the graph. Example of output: [[1,2], [1,3], [3,2]]
		"""
		
		edges = []

		for line in self.readed_graph[1:]:
			line = line.split(' ')
			edges.append([int(line[0]), int(line[1])])
		return edges

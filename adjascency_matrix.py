# to do: minimum graph degree, maximum graph degree, mean graph degree and median graph degree
from graph import Graph


class AdjascencyMatrix:
	def __init__(self, file_name):
		self.graph = Graph(file_name)
		self.matrix =  [[0 for i in range(self.graph.vertices_quantity)] 
										for j in range(self.graph.vertices_quantity)]
		
		self.build_representation()

	def build_representation(self):
		for edge in self.graph.edges:
			self.add_edge(edge[0], edge[1])

	def add_edge(self, s, d):
		self.matrix[s][d] = 1
		self.matrix[d][s] = 1

	def node_neighbors(self, node):
		neighbors = []
		for node_elem in range(len(self.matrix)):
			if self.matrix[node][node_elem] == 1:
					neighbors.append(node_elem)
    
		return neighbors

	def node_degree(self, node):
		""" 
				It's the same as the quantity of node's edges
		"""
		return sum(self.matrix[node])
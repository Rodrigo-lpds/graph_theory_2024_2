
class TreeGraph:
    def __init__(self, root):
        self.tree_graph = {}
        self.insert_vertex_node(root, 0, 0)

    def add_vertex_node(self, vertex, dad):
        """
		Try to add a Vertex to the tree and calculate his nivel, return true if vertex doesn't exist in the tree
		"""
        if(self.tree_graph.get(vertex) is None):
            nivel = self.tree_graph[dad].nivel + 1
            self.insert_vertex_node(vertex, dad, nivel)
            return True
        else:
            return False

    def insert_vertex_node(self, vertex, dad, nivel):
        """
		Insert a Vertex in the tree
		"""
        node = TreeNode(vertex, dad, nivel, True)
        self.tree_graph.update({vertex: node})
    
    def print_tree(self):
        for value in self.tree_graph.values():
            value.print_node()
    
    def distance_between_vertex(self, vertex):
        distance = self.tree_graph[vertex].nivel
        print("distance:", distance)
    
    def longest_short_path(self):
        last_explored_node = list(self.tree_graph.keys())[-1]
        distance = self.tree_graph[last_explored_node].nivel

        return distance

    def explored_node(self,index):
        return list(self.tree_graph.keys())[index]

class TreeNode:
    def __init__(self, vertex, dad, nivel, is_explored):
        self.vertex = vertex
        self.dad = dad
        self.is_explored = is_explored
        self.nivel = nivel

    def print_node(self):
        print("vertex:", self.vertex, "dad:", self.dad, "nivel:", self.nivel)
    
    def set_explored(self, is_explored):
        self.is_explored = is_explored
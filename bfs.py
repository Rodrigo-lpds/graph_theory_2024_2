from tree_graph import TreeGraph

class BuildBFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.tree = TreeGraph(self.root)
        self.build_tree()

    def build_tree(self):
        queue = [self.root]
        while(len(queue) > 0):
            currentVertex = queue.pop(0)
            for neighbor in self.graph.node_neighbors(currentVertex): # use graph representation instead
                if(self.tree.add_vertex_node(neighbor, currentVertex)):
                    queue.append(neighbor)



    def represent_tree(self):
        self.tree.print_tree()

    def distance_between_vertex(self, vertex):
        self.tree.distance_between_vertex(vertex)
    
    def longest_short_path(self):
        return self.tree.longest_short_path()
    
    def explored_node(self, index):
        return self.tree.explored_node(index)
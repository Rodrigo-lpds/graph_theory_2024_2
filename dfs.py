from tree_graph import TreeGraph

class BuildDFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.tree = TreeGraph(self.root)
        self.build_tree()

    def build_tree(self):
        stack = [self.root]
        explored_vertices = []
        while(len(stack) > 0):
            currentVertex = stack.pop(0)
            if currentVertex not in explored_vertices:
                explored_vertices.append(currentVertex)
                for neighbor in self.graph.node_neighbors(currentVertex):
                    self.tree.add_vertex_node(neighbor, currentVertex)
                    stack.append(neighbor)


    def represent_tree(self):
        self.tree.print_tree()



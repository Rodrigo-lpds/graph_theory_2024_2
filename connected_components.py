from tkinter.tix import Tree
from tree_graph import TreeGraph


class ConnectedComponentes:
    def __init__(self, graph):
        self.graph = graph.get_nodes_graph()
        self.components = []
        self.find_connected_components()

    def find_connected_components(self):
        nodes = self.graph.values()
        self.find_new_component(nodes)

    def find_new_component(self, nodes):
        for node in nodes:
            if(node.explored is False):
                self.components.append([])
                component_index = len(self.components) - 1
                self.explore_node(node, component_index)

    def explore_node(self, root, component_index):
        queue = [root]
        while(len(queue)>0):
            new_node = queue.pop(0)
            for neighbor in new_node.get_neighbors_nodes():
                if(neighbor.explored is False):
                    neighbor.explored = True
                    self.components[component_index].append(neighbor)
                    queue.append(neighbor)
    
    
    def represent_components(self):
        self.sort_components()
        index = 0
        for component in self.components:
            vertices_list = []
            index += 1
            print("Size of Component " + str(index) + " : " + str(len(component)))
            #for node in component:
            #    vertices_list.append(node.get_name())
            #print("Vertices of Component "+ str(index)+ " : " + str(vertices_list))
            print()

    def sort_components(self):
        for iter_num in range(len(self.components)-1,0,-1):
            for index in range(iter_num):
                if len(self.components[index]) < len(self.components[index+1]):
                    temp = self.components[index]
                    self.components[index] = self.components[index+1]
                    self.components[index+1] = temp     
# Import statistics Library
from math import degrees
import statistics

class GraphInfoOutput:
    def __init__(self, graph_rep):
        self.graph_rep = graph_rep
        self.degree_list = []
        
    
    def build_file(self, file_name):
        self.list_node_degrees()
        
        f = open(file_name, "w")
        f.write("Grafo do arquivo: " + self.graph_rep.graph.file_name + "\n")
        f.write("Quantidade de vertices: " + str(self.nodes_quantity()) + "\n")
        f.write("Numero de Arestas: " + str(self.edges_quantity()) + "\n")
        f.write("Grau mínimo: " + str(self.minimum_degree())+ "\n")
        f.write("Grau máximo: " + str(self.maximum_degree()) + "\n")
        f.write("Grau médio: " + str(self.mean_degree()) + "\n")
        f.write("Mediana de grau: " + str(self.median_degree()) + "\n")
        f.close()
    
    def nodes_quantity(self):
        return self.graph_rep.graph.vertices_qty()
    
    def edges_quantity(self):
        return len(self.graph_rep.graph.edges_array())
    
    def list_node_degrees(self):
        node_list = self.graph_rep.node_list()
        for node in node_list:
            self.degree_list.append(self.graph_rep.node_degree(node))
        return self.degree_list
            
        
    def minimum_degree(self):
        return min(self.degree_list)
    
    def maximum_degree(self):
        return max(self.degree_list)
    
    def mean_degree(self):
        return statistics.mean(self.degree_list)
    
    def median_degree(self):
        return statistics.median(self.degree_list)
    #def connected_components(self)
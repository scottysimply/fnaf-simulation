class DiGraph:
    def __init__(self, adjacency: dict, values: dict):
        for key, adj in adjacency.items():
            if key not in values:
                raise KeyError("Key in adjacency not found in values!")
        self.adjacency = adjacency
        self.values = values

    def get_subgraph(self, nodes: list):
        """
        Obtains a subgraph that includes each node.

        nodes: Should be the key of each node.
        """
        sub_adj = {}
        sub_values = {}
        for node in nodes:
            if node in self.adjacency and node in self.values:
                sub_adj[node] = self.adjacency[node]
                sub_values[node] = self.values[node]
        return DiGraph(sub_adj, sub_values)
    
    def get_adjacents_subgraph(self, node):
        return self.get_subgraph(self.adjacency[node])
"""
in_degree_distribution
"""

EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}

def make_complete_graph(num_nodes):
    """ @todo: Docstring for function.

    :num_nodes: the number of nodes
    :returns: a dictionary corresponding to a complete directed graph with the
              specified number of nodes.

    """
    graph = {}

    for node in xrange(num_nodes):
        graph[node] = set([])
        for adj_node in xrange(num_nodes):
            if node == adj_node:
                continue
            graph[node].add(adj_node)

    return graph

def compute_in_degrees(digraph):
    """ @todo: Docstring for function.

    :arg1: a directed graph
    :returns: a dictionary with the same set of keys (nodes) as digraph whose
              corresponding values are the number of edges whose head matches a
              particular node.

    """
    in_degree_dic = {}

    for node in digraph.keys():
        in_degree_dic.setdefault(node, 0)

    for adj_nodes in digraph.values():
        for adj_node in adj_nodes:
            in_degree_dic[adj_node] += 1

    return in_degree_dic


def in_degree_distribution(digraph):
    """ @todo: Docstring for function.
    :arg1: a directed graph
    :returns: The function should return a dictionary whose keys correspond to
              in-degrees of nodes in the graph. The value associated with each
              particular in-degree is the number of nodes with that in-degree.
              In-degrees with no corresponding nodes in the graph are not
              included in the dictionary.

    """
    in_degree_dist = {}
    out_degress = {}
    lonely_node = {}

    for node, adjacency in digraph.items():
        lonely_node[node] = True

    for node, adjacency in digraph.items():
        for dummy_i in adjacency:
            out_degress.setdefault(dummy_i, 0)
            out_degress[dummy_i] += 1
            lonely_node[dummy_i] = False

    #  return out_degress
    for out_direction in out_degress.values():
        in_degree_dist.setdefault(out_direction, 0)
        in_degree_dist[out_direction] += 1

    # look for lonely node
    if len([1 for i in lonely_node.values() if i == True]):
        in_degree_dist[0] = \
            len(digraph) - len([1 for i in lonely_node.values() if i == False])

    return in_degree_dist

def main():
    """
    bala bala
    """
    #  import alg_module1_graphs

    #  print make_complete_graph(0)
    #  print make_complete_graph(1)
    print make_complete_graph(10)

    #  print compute_in_degrees(EX_GRAPH0)
    #  print compute_in_degrees(EX_GRAPH1)
    #  print compute_in_degrees(EX_GRAPH2)
    #  print compute_in_degrees(alg_module1_graphs.GRAPH0)
    #  print compute_in_degrees(alg_module1_graphs.GRAPH1)
    #  print compute_in_degrees(alg_module1_graphs.GRAPH2)
    #  print compute_in_degrees(alg_module1_graphs.GRAPH3)
    #  print compute_in_degrees(alg_module1_graphs.GRAPH4)
    #  print compute_in_degrees(alg_module1_graphs.GRAPH5)
    #  print compute_in_degrees(alg_module1_graphs.GRAPH6)
    #  print compute_in_degrees(alg_module1_graphs.GRAPH7)
    #  print compute_in_degrees(alg_module1_graphs.GRAPH8)

    #  print in_degree_distribution(EX_GRAPH0)
    #  print in_degree_distribution(EX_GRAPH1)
    #  print in_degree_distribution(EX_GRAPH2)
    #  print in_degree_distribution(alg_module1_graphs.GRAPH0)
    #  print in_degree_distribution(alg_module1_graphs.GRAPH1)
    #  print in_degree_distribution(alg_module1_graphs.GRAPH2)
    #  print in_degree_distribution(alg_module1_graphs.GRAPH3)
    #  print in_degree_distribution(alg_module1_graphs.GRAPH4)
    #  print in_degree_distribution(alg_module1_graphs.GRAPH5)
    #  print in_degree_distribution(alg_module1_graphs.GRAPH6)
    #  print in_degree_distribution(alg_module1_graphs.GRAPH7)
    #  print in_degree_distribution(alg_module1_graphs.GRAPH8)
    #  print in_degree_distribution(alg_module1_graphs.GRAPH9)

if __name__ == '__main__':
    main()

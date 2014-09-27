import math
import matplotlib.pyplot as plt
from in_degree_distribution import *

def load_citation_graph():
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    with open("alg_phys-cite.txt", "r") as graph_file:
        #  graph_file = urllib2.urlopen(graph_url)
        graph_text = graph_file.read()
        graph_lines = graph_text.split('\n')
        graph_lines = graph_lines[ : -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

def main():
    citation_graph = load_citation_graph()

    in_degress_dis = in_degree_distribution(citation_graph)
    plot_size = sum(in_degress_dis.values())

    # normalize the distribution
    # (make the values in the dictionary sum to one)
    for in_degress in in_degress_dis:
        in_degress_dis[in_degress]/=float(plot_size)

    plot = []
    #  for input_val in range(plot_size):
    for input_val in range(2, plot_size):
        if not in_degress_dis.get(input_val): continue

        counter = in_degress_dis[input_val]
        plot.append([input_val, counter])

    plot_x = lambda xy: [x[0] for x in xy]
    plot_y = lambda xy: [x[1] for x in xy]

    plt.loglog(plot_x(plot), plot_y(plot))
    plt.xlabel('Input')
    plt.ylabel('Counter')
    plt.title('Iteration counts')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()


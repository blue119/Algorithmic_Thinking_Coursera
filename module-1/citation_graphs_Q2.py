import random
import math
import matplotlib.pyplot as plt
from in_degree_distribution import *

def Alg_ER(n, p):
    """
    :arg1: number of nodes
    :arg2: probability
    :returns: a directe graph
    """
    graph = {}
    for i in xrange(1, n+1):
        graph[i] = set()

    for i in xrange(1, n+1):
        for j in xrange(1, n+1):
            if i == j: continue
            if p < random.random(): graph[i].add(j)

    return graph

def Mod_Alg_ER(n, p):
    """
    :arg1: number of nodes
    :arg2: probability
    :returns: a directe graph
    """
    graph = {}
    for i in xrange(1, n+1):
        graph[i] = set()

    for i in xrange(1, n+1):
        for j in xrange(1, n+1):
            if i == j: continue
            if p < random.random(): graph[i].add(j)
            graph[j].add(i)

    return graph

def main():
    #  pp = [0.45, 0.5, 0.55]
    pp = [0.55]
    ns = 1000
    for p in pp:
        citation_graph = Alg_ER(ns, p)

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

            #  plot.append([math.log(input_val), math.log(counter)])
        plot2 = []
        for input_val, counter in plot:
            plot2.append([math.log(input_val), math.log(counter)])

        #  plt.loglog(plot_x(plot), plot_y(plot), color = 'r')
        plt.plot(plot_x(plot2), plot_y(plot2), color = 'r')
        plt.plot(plot_x(plot), plot_y(plot), color = 'g')
        plt.xlabel('Input')
        plt.ylabel('Counter')
        plt.title('Nodes(%d), P(%.2f)' % (ns, p))
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    main()

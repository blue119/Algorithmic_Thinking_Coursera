""" bala bala
"""

from collections import deque

def bfs_visited(ugraph, start_node):
    """@todo: Docstring for bfs_visited.

    :ugraph: @todo
    :start_node: @todo
    :returns: @todo

    """
    visited = []
    _qq = deque()

    _qq.append(start_node)
    visited.append(start_node)

    while _qq:
        _jj = _qq.pop()
        for _hh in ugraph[_jj]:
            #  print "%d -> %d" % (j, h)
            if _hh not in visited:
                visited += [_hh]
                _qq.append(_hh)
                #  print Q
    return set(visited)

def cc_visited(ugraph):
    """@todo: Docstring for cc_visited.

    :ugraph: @todo
    :returns: @todo

    """
    from random import shuffle
    remaining_node = ugraph.keys()
    _cc = []

    shuffle(remaining_node)
    while remaining_node:
        _ii = remaining_node.pop()
        _ww = bfs_visited(ugraph, _ii)
        #  print i, W
        if set(_ww) not in _cc:
            _cc.append(set(_ww))

    return _cc

def largest_cc_size(ugraph):
    """@todo: Docstring for largest_cc_size.

    :ugraph: @todo
    :returns: @todo

    """
    if not ugraph:
        return 0
    return max(map(len, cc_visited(ugraph)))

def compute_resilience(ugraph, attach_order):
    """@todo: Docstring for compute_resilience.

    :ugraph: @todo
    :attach_order: @todo
    :returns: @todo

    """
    def _ugraph_pop(ugraph, _nn):
        """ bala bala
        """
        #  new_graph
        del ugraph[_nn]
        #  print ugraph
        for _ii in ugraph:
            #  print i
            if _nn in ugraph[_ii]:
                ugraph[_ii].remove(_nn)
        return ugraph

    _attach_order = attach_order[:]
    _ugraph = ugraph.copy()

    return_list = [largest_cc_size(_ugraph)]
    while _attach_order:
        _ii = _attach_order.pop(0)
        _ugraph = _ugraph_pop(_ugraph, _ii)
        #  print _ugraph
        return_list.append(largest_cc_size(_ugraph))
    #  print _ugraph_pop(ugraph, 3)
    return return_list

def main():
    """@todo: Docstring for main.
    :returns: @todo

    """
    ugraph = {
        0: set([1]),
        1: set([0, 2]),
        2: set([1]),
    }

    #  ugraph = GRAPH0
    #  from random import shuffle
    #  print bfs_visited(ugraph, 0)
    print cc_visited(ugraph)
    print largest_cc_size(ugraph)
    #  order = EX_GRAPH1.keys()
    #  shuffle(order)
    print compute_resilience(ugraph, [1, 0, 2])
    #  print compute_resilience(ugraph, [1, 2])
    #  print bfs_visited(EX_GRAPH2, 0)


if __name__ == '__main__':
    main()

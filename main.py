from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    # Dijkstra's algorithm where the "distance" of a path is the pair
    # (total weight, number of edges), compared lexicographically. Ties in
    # weight are then broken in favor of fewer edges automatically.
    #
    # This is still correct because extending a path by an edge with
    # positive weight w changes its pair from (d, e) to (d + w, e + 1), which
    # is strictly larger lexicographically. So the first time a vertex is
    # popped off the heap, its pair is minimal, exactly as in Dijkstra.
    result = {}
    frontier = [(0, 0, source)]   # (path weight, number of edges, vertex)
    while frontier:
        weight, edges, v = heappop(frontier)
        if v in result:
            continue              # stale entry; v already finalized
        result[v] = (weight, edges)
        for u, w in graph[v]:
            if u not in result:
                heappush(frontier, (weight + w, edges + 1, u))
    return result
    

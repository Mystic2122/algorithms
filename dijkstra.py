""" 
Graph is of the form {node1 : [(node2, d2), (node4, d4)], node2 : [(node1, d1),...], ...}

"""
import sys


def dijkstra(graph: dict[str, list[tuple[str, int]]], start: str) -> int:
    visited = [False] * len(graph)
    min_distances = [sys.maxsize] * len(graph)

    verticies = list(graph.keys())

    cur_idx = verticies.index(start)

    # Assume its zero-cost to traverse to same node
    min_distances[cur_idx] = 0
    visited[cur_idx] = True
    cur_node = start
    while False in visited:
        connections = graph[cur_node]

        # Update shortest paths from current node
        for connection in connections:
            connection_idx = verticies.index(connection[0])
            if min_distances[cur_idx] + connection[1] < min_distances[connection_idx]:
                min_distances[connection_idx] = min_distances[cur_idx] + connection[1]
        
        # Select next untraversed node
        cur_min = sys.maxsize
        for i in range(len(min_distances)):
            if visited[i] == False and min_distances[i] < cur_min:
                cur_min = i
        cur_node = verticies[cur_min]
        cur_idx = cur_idx = verticies.index(cur_node)
        visited[cur_min] = True

    
    return min_distances


graph = {"A" : [("B", 1), ("C", 2), ("E", 7)], "B" : [("A",1),("C",3), ("D",3)], "C" : [("A", 2), ("B", 3),("D", 4)], "D" : [("B", 3),("C", 4),("E", 2)], "E" : [("A",7),("D", 2)]}


print(dijkstra(graph, "A"))

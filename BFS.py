graph = {'A': ['E', 'B', 'D'],
         'B': ['A', 'D', 'C'],
         'C': ['B'],
         'D': ['A', 'B'],
         'E': ['A']
         }


def bfs_connected_component(graph, start):
    queue = [start]
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue = queue + graph[node]
    return visited


print(bfs_connected_component(graph, 'A'))  # return

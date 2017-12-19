graph = {'A': ['B'],
         'B': ['E', 'C', 'D'],
         'C': ['A', 'D'],
         'D': [],
         'E': ['F'],
         'F': ['D']
         }


def dfs(graph, s):  # s is the source node of the graph
    stack = []  # to put the nodes onto the stack
    visited = []  #
    stack = [s]  # put  the source node onto the stack
    while stack:
        node = stack.pop()  # pop th node from the stack
        if node not in visited:  # to ensue that one node comes only onces
            visited.append(node)
            if graph[node]:
                stack = stack + graph[
                    node]  # put the node which is connected to the poped node   cancatinate the value of the dictionary to the list
    return visited


print(graph)
print(dfs(graph, 'A'))  # node is A so it returns the output
print(dfs(graph, 'B'))
print(dfs(graph, 'C'))
print(dfs(graph, 'D'))
print(dfs(graph, 'E'))


# machine learning
# cloud of things
# robotics
# cybersecurity
# iot
# big data
#


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
    return visited

def connected_component(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            connected_component(graph, start, visited)
    return visited

# def dfs_paths(graph, start, end):
#     stack = [(start, [start])]
#     while stack:
#         (vertex,path) = stack.pop()
#         for next in graph[vertex] - set(path)
#             if next == goal:
#                 yield path + [next]
#             else:
#                 stack.append((next, path  + [next]))


print dfs(graph, 'A')
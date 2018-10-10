# graph = {'A': set(['B', 'C']),
#          'B': set(['A', 'D', 'E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B', 'F']),
#          'F': set(['C', 'E'])}

graph = { '2': set(['0', '3']),
          '3': set(['3']),
          '0': set(['2', '1']),
          '1': set(['2'])
}

# level by level
def bfs(graph, start):
    visited = {}

    for node in graph:
        visited[node] = False
    queue = []

    queue.append(start)
    visited[start] = True

    while queue:
        vertex = queue.pop(0)
        print vertex
        for i in graph[vertex]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
# recurse all the way down. then next
def dfs(graph, start):
    visited = {}

    visited = {vertex: False for vertex in graph}

    explore(start, visited)

def explore(v, visited):

    visited[v] = True
    print v
    for node in graph[v]:
        if visited[node] == False:
            explore(node, visited)


def dijkstra(graph, source, dest):
    inf = float('inf')
    # distances from source to other nodes in graph
    distances = {vertex: inf for vertex in graph}
    distance[start] = 0

    # node that is previous to current node
    previous = {vertex: None for vertex in graph}

    vertices = graph.copy()
    while vertices:
        current_vertex = min(vertices)
        visited[current] = True

        for adjacent in graph[current]:
            if visited[adjacent]:
                continue
            # new_distance = distance[adjacent] +



    print distances
# dijkstra(graph, '2', '0')
dfs(graph, '2')
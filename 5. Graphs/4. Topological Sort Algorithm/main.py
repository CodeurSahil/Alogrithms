def topologicalSort(edges, n):
    adj = {}

    for i in range(n):
        adj[i] = []

    for src, dest in edges:
        adj[src].append(dest)

    topo = []
    visited = set()

    for i in range(n):
        dfs(adj, i, visited, topo)

    topo.reverse()

    return topo

def dfs(list, node, visited, topo):
    if node in visited:
        return
    
    visited.add(node)

    for neigh in list[node]:
        dfs(list, neigh, visited, topo)

    topo.append(node)

print(
    topologicalSort(
        [
    (0,1),
    (0,2),
    (1,3),
    (2,3)
], 4
    )
)
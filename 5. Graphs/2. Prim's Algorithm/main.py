import heapq

def prims (edges, n):
    adj = {}

    for i in range(n):
        adj[i] = []

    for s, d, w in edges:
        adj[s].append((d, w))
        adj[d].append((s, w))

    minHeap = []

    for n, w in adj[0]:
        heapq.heappush(minHeap, (w, 0, n))

    mst = []
    visited = set()
    visited.add(0)

    while minHeap:
        w1, s1, node = heapq.heappop(minHeap)

        if node in visited:
            continue

        mst.append([s1, node])
        visited.add(node)

        for neigh, w2 in adj[node]:
            if neigh not in visited:
                heapq.heappush(minHeap, (w1 + w2, node, neigh))

    return mst

print(
    prims(
        [
    (0,1,4),
    (0,2,1),
    (2,1,2),
    (1,3,1),
    (2,3,5)
], 4
    )
)

print(
    prims(
        [
    (0,1,2),
    (0,3,6),
    (1,2,3),
    (1,3,8),
    (1,4,5),
    (2,4,7),
    (3,4,9)
], 5
    )
)

import heapq

def dijkstra (edges, n, src):
    adj = {}

    for i in range(n):
        adj[i] = []

    for s, d, w in edges:
        adj[s].append((d, w))

    shortest = {}
    minHeap = [(0, src)]

    while minHeap:
        w1, n1 = heapq.heappop(minHeap)

        if n1 in shortest:
            continue

        shortest[n1] = w1

        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minHeap, (w1 + w2, n2))

    return shortest

print(
    dijkstra(
        [
    (0,1,4),
    (0,2,1),
    (2,1,2),
    (1,3,1),
    (2,3,5)
], 4, 0
    )
)

print(
    dijkstra(
        [
    (0,1,10),
    (0,2,3),
    (1,2,1),
    (2,1,4),
    (2,3,2),
    (1,3,2),
    (3,4,7)
], 5, 0
    )
)

print(
    dijkstra(
    [
    (0,1,1),
    (1,2,2),
    (2,0,4),
    (1,3,6),
    (2,3,3)
    ], 4, 0
    )
)

print(
    dijkstra(
        [
    (0,1,2),
    (0,2,4),
    (1,2,1),
    (1,3,7),
    (2,4,3),
    (4,3,2),
    (3,5,1),
    (4,5,5)
        ], 6, 0
    )
)

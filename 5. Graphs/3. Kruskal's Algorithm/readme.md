# Kruskal's Algorithm

## What is Kruskal's Algorithm?

Kruskal's Algorithm is a **greedy algorithm** that finds the **Minimum Spanning Tree (MST)** of a weighted, connected, undirected graph. It builds the MST by sorting all edges and greedily adding edges in order of increasing weight, as long as they don't create a cycle.

---

## Why Do We Need It?

Kruskal's algorithm is essential for solving **Minimum Spanning Tree problems** in real-world applications:

- **Network Design**: Building cost-efficient communication networks with minimum infrastructure cost
- **Electrical Grids**: Connecting power stations with minimum cable length/cost
- **Airline Routes**: Creating flight networks with minimum total distance
- **Water Distribution Networks**: Connecting cities with minimum pipe length
- **Road Networks**: Building highway systems with minimum cost
- **Telecommunications**: Designing efficient transmission networks
- **Cluster Analysis**: Hierarchical clustering in machine learning
- **Circuit Design**: Connecting circuit components with minimum wire length

---

## How It Works

### Algorithm Steps:

1. **Sort All Edges**:
   - Create a list of all edges in the graph
   - Sort edges by weight in ascending order

2. **Initialize Union-Find**:
   - Create a Disjoint Set Union (DSU) data structure
   - Initially, each vertex is in its own set

3. **Build MST**:
   - For each edge (in sorted order):
     - Check if the two vertices are in different sets using `find()`
     - If yes, add edge to MST and `union()` the two sets
     - If no, skip (would create a cycle)

4. **Terminate**: When MST has V-1 edges, it's complete

### Key Principle:
- Always add the edge with the **smallest weight** that doesn't create a cycle
- Uses **Union-Find** to efficiently detect cycles

---

## Complexity Analysis

### Time Complexity: **O(E log E)**

Where:
- **V** = number of vertices (nodes)
- **E** = number of edges

Breaking it down:
- Sorting edges: **O(E log E)**
- Union-Find operations: **O(E * α(V))** where α is inverse Ackermann (almost constant)
- Total: **O(E log E + E * α(V)) ≈ O(E log E)**

Since sorting dominates, the final complexity is **O(E log E)**.

### Space Complexity: **O(V + E)**

- `minHeap`: **O(E)** for storing all edges
- Union-Find structures (`par`, `rank`): **O(V)**
- `mst` list: **O(V)** (V-1 edges)
- **Total: O(V + E)**

---

## Union-Find (Disjoint Set Union) Explained

Union-Find is a data structure with two main operations:

### 1. **Find(x)** - O(α(V))
- Finds the representative (parent) of the set containing x
- Uses **path compression**: updates parent pointers during search
- Makes future searches faster

### 2. **Union(x, y)** - O(α(V))
- Merges the sets containing x and y
- Uses **union by rank**: attaches smaller tree to larger tree
- Keeps tree height minimal

### Path Compression:
```python
def find(self, n):
    p = self.par[n]
    while p != self.par[p]:
        self.par[p] = self.par[self.par[p]]  # Updates parent pointer
        p = self.par[p]
    return p
```

### Union by Rank:
```python
def union(self, n1, n2):
    p1, p2 = self.find(n1), self.find(n2)
    
    if p1 == p2:
        return False  # Already in same set (would create cycle)
    
    # Attach smaller tree to larger tree
    if self.rank[p1] > self.rank[p2]:
        self.par[p2] = p1
    else:
        self.par[p1] = p2
        if self.rank[p1] == self.rank[p2]:
            self.rank[p2] += 1
    
    return True  # Successfully merged
```

---

## Prerequisites & Constraints

### ✅ When Kruskal's Works:
- **Undirected weighted graphs**
- All edge weights must be **non-negative**
- Graph must be **connected** (to find MST for entire graph)
- Works well with **sparse graphs**

### ❌ When Kruskal's Doesn't Work:
- **Directed graphs** (use modified versions)
- **Negative edge weights**
- **Disconnected graphs** (will find MST for each component)

---

## Implementation Details

### Data Structures Used:
1. **Min-Heap**: Stores all edges sorted by weight
2. **Union-Find**:
   - `par`: Dictionary mapping each node to its parent
   - `rank`: Dictionary tracking tree height for each root
3. **List (mst)**: Stores edges in the minimum spanning tree

### Algorithm Advantages:
- ✅ Excellent for **sparse graphs** (better than Prim's)
- ✅ Optimal and simple greedy approach
- ✅ Works well when edges are already sorted
- ✅ Can be parallelized for distributed computing
- ✅ Union-Find enables efficient cycle detection

### Limitations:
- ❌ Requires sorting all edges: **O(E log E)**
- ❌ Extra space for storing all edges
- ❌ Less efficient than Prim's for dense graphs
- ❌ Doesn't work with negative edge weights

---

## Use Cases & Examples

### Real-World Applications:
1. **ISP Networks**: Connecting cities with minimum cable cost
2. **Electrical Grids**: Connecting power stations with minimum infrastructure
3. **Road Construction**: Building highway networks with minimum cost
4. **Airline Networks**: Connecting airports with minimum total distance
5. **Data Center Networks**: Connecting servers with minimum latency
6. **Biological Networks**: Analyzing protein interactions
7. **Game Development**: Creating efficient terrain connections

### Problems to Solve:
- Find minimum spanning tree of a graph
- Minimum cost to connect all houses with roads
- Most efficient way to connect N cities
- Network design with minimum total transmission distance

---

## Example Walkthrough

### Example 1: Simple Graph (4 nodes)
```
Graph:
0 -- 1 (weight 1)
1 -- 2 (weight 2)
2 -- 3 (weight 3)
3 -- 0 (weight 4)
0 -- 2 (weight 5)

Edges sorted by weight:
[(1, 0, 1), (2, 1, 2), (3, 2, 3), (4, 3, 0), (5, 0, 2)]

Kruskal's Process:
1. Add edge (0,1, weight 1): Union(0,1) → {0,1}, {2}, {3}  ✓
2. Add edge (1,2, weight 2): Union(1,2) → {0,1,2}, {3}      ✓
3. Add edge (2,3, weight 3): Union(2,3) → {0,1,2,3}         ✓
4. Skip edge (3,0, weight 4): Find(3)==Find(0) → Cycle!  ✗
5. Skip edge (0,2, weight 5): Find(0)==Find(2) → Cycle!  ✗

Output (MST):
[[0, 1], [1, 2], [2, 3]]

Total Weight: 1 + 2 + 3 = 6
Number of Edges: 3 (which is V-1 for 4 nodes)
```

**Step-by-Step Union-Find:**
```
Initial: {0}, {1}, {2}, {3}
After union(0,1): {0,1}, {2}, {3}
After union(1,2): {0,1,2}, {3}
After union(2,3): {0,1,2,3}
```

---

## Comparison with Prim's Algorithm

| Aspect | Kruskal's | Prim's |
|--------|-----------|--------|
| **Approach** | Sort edges globally | Grow tree locally from vertex |
| **Data Structure** | Heap + Union-Find | Min-heap + Visited set |
| **Time Complexity** | O(E log E) | O(E log V) |
| **Edge Sorting** | Required | Not required |
| **Best For** | Sparse graphs | Dense graphs |
| **Implementation** | Slightly complex | Simpler |
| **Parallelizable** | ✅ Yes | ❌ Difficult |

### When to Use Which:
- **Kruskal's**: E < V² (sparse graphs)
- **Prim's**: E ≈ V² (dense graphs)
- Example: For V=100, if E<10,000 use Kruskal's, else use Prim's

---

## Properties of Minimum Spanning Tree

- **V-1 edges**: An MST has exactly V-1 edges for V vertices
- **Connected**: Connects all V vertices
- **Acyclic**: No cycles in the MST
- **Minimum Weight**: Total edge weight is minimal
- **Cut Property**: Every edge in MST is the minimum weight edge crossing some cut
- **Cycle Property**: The heaviest edge in any cycle is not in any MST

---

## Advanced Concepts

### Why Union-Find Works:
Union-Find efficiently answers the question: **"Are two nodes already connected?"**
- Without it, checking connectivity would take O(V) per edge
- With Union-Find + path compression, it takes nearly O(1)

### Why Path Compression Matters:
```
Before: 1 → 2 → 3 → 4 → 4 (4 hops)
After:  1 → 4 ↗ 4 ↗ 4 (all point to 4)
```
Flattens the tree structure for faster future queries.

### Cycle Detection:
```
if find(node1) == find(node2):
    # They're already in same component
    # Adding edge would create a cycle
```

---

## Comparison with Other MST Algorithms

| Algorithm | Time | Best For | MST? |
|-----------|------|----------|------|
| **Kruskal's** | O(E log E) | Sparse graphs | ✅ Yes |
| **Prim's** | O(E log V) | Dense graphs | ✅ Yes |
| **Borůvka's** | O(E log V) | Parallel processing | ✅ Yes |
| **Dijkstra's** | O((V+E) log V) | Shortest path (not MST) | ❌ No |

---

## Key Takeaways

✨ **Remember:**
1. Kruskal's finds the **Minimum Spanning Tree** in **O(E log E)** time
2. It works optimally with **non-negative edge weights**
3. It uses **Union-Find** for efficient cycle detection
4. Best suited for **sparse graphs**
5. Always considers the **globally smallest edge** first
6. The MST has exactly **V-1 edges** for V vertices
7. Path compression and union by rank make Union-Find nearly O(1)
8. Real-world applications: network design, infrastructure, clustering

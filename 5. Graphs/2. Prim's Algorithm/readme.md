# Prim's Algorithm

## What is Prim's Algorithm?

Prim's Algorithm is a **greedy algorithm** that finds the **Minimum Spanning Tree (MST)** of a weighted, connected, undirected graph. A minimum spanning tree is a subgraph that includes all vertices with the minimum total edge weight.

---

## Why Do We Need It?

Prim's algorithm is essential for solving **Minimum Spanning Tree problems** in real-world applications:

- **Network Design**: Building cost-efficient networks (telecommunications, utility grids, roads)
- **Electrical Grids**: Connecting power stations with minimum cable length/cost
- **Airline Routes**: Creating flight networks with minimum travel distance
- **Computer Networks**: Designing efficient network topologies with minimum bandwidth
- **Circuit Design**: Connecting electronic components with minimum wire length
- **Cluster Analysis**: Grouping data points with minimum distances
- **Image Processing**: Segmentation and edge detection
- **Telecommunication Networks**: Building efficient phone networks with minimum infrastructure costs

---

## How It Works

### Algorithm Steps:

1. **Initialize**:
   - Start with an arbitrary vertex (usually vertex 0)
   - Mark it as visited
   - Add all edges from this vertex to the min-heap

2. **Build MST**:
   - Extract the edge with minimum weight from the heap
   - If the destination vertex is not visited:
     - Add this edge to the MST
     - Mark destination as visited
     - Add all edges from the destination vertex to the heap
   - If destination is already visited, skip this edge

3. **Terminate**: When all vertices are visited, the MST is complete

### Key Principle:
- Always add the edge with the **smallest weight** that connects a visited vertex to an unvisited vertex
- This greedy choice guarantees the minimum total weight for the spanning tree

---

## Complexity Analysis

### Time Complexity: **O(E log V)**

Where:
- **V** = number of vertices (nodes)
- **E** = number of edges

Breaking it down:
- We visit each edge once: **O(E)**
- Each heap operation (push/pop) takes: **O(log E)** or **O(log V)**
- Since E ≤ V² in most practical graphs: **O(E log V)**

**Note**: With a Fibonacci heap, this can be optimized to **O(E + V log V)**.

### Space Complexity: **O(V + E)**

- `adj` dictionary storing adjacency list: **O(V + E)**
- `visited` set: **O(V)**
- Min-heap in worst case: **O(E)**
- `mst` list: **O(V)**
- **Total: O(V + E)**

---

## Prerequisites & Constraints

### ✅ When Prim's Works:
- **Undirected weighted graphs**
- All edge weights must be **non-negative**
- Graph must be **connected** (to find MST for entire graph)
- Can handle isolated components with modification

### ❌ When Prim's Doesn't Work:
- **Directed graphs** (use modified version)
- **Negative edge weights** (MST concept breaks down)
- **Disconnected graphs** (won't span all nodes)

---

## Implementation Details

### Data Structures Used:
1. **Dictionary (adj)**: Stores the graph as an adjacency list (undirected)
2. **Set (visited)**: Tracks which vertices are already in the MST
3. **Min-Heap**: Maintains edges by weight for efficient extraction of minimum
4. **List (mst)**: Stores the edges that form the minimum spanning tree

### Algorithm Advantages:
- ✅ Efficient for dense graphs (O(E log V) when E is large)
- ✅ Optimal for complete or near-complete graphs
- ✅ Single pass through the graph
- ✅ Intuitive greedy approach
- ✅ Good for practical applications like network design

### Limitations:
- ❌ Doesn't work with negative edge weights
- ❌ Requires connected graph to find single MST
- ❌ Less efficient than Kruskal's for sparse graphs

---

## Use Cases & Examples

### Real-World Applications:
1. **Infrastructure Networks**: Road networks, water pipes, power lines with minimum cost
2. **Telecommunications**: Building phone networks with minimum cable distance
3. **Computer Networks**: Designing efficient network topologies
4. **Airline Networks**: Connecting cities with minimum total flight distance
5. **Circuit Board Design**: Connecting electronic components with minimum wire
6. **Image Processing**: Scene segmentation and edge detection
7. **Clustering Algorithms**: Hierarchical clustering in data mining

### Problems to Solve:
- Find minimum spanning tree of a graph
- Connect N cities with minimum total distance
- Design a network with minimum cost
- Partition a graph into connected components

---

## Example Walkthrough

### Example 1: Simple Graph (4 nodes)
```
Graph:
0 -- 1 (weight 4)
0 -- 2 (weight 1)
2 -- 1 (weight 2)
1 -- 3 (weight 1)
2 -- 3 (weight 5)

Starting from node 0

Prim's Output (MST):
[[0, 2], [2, 1], [1, 3]]

Total Weight: 1 + 2 + 1 = 4
```

**Step-by-Step:**
1. Start with node 0 (visited: {0})
2. Add edges: (1, 0, 1), (4, 0, 1) to heap
3. Pop (1, 0, 2): Add [0, 2], visited: {0, 2}
4. Add edges to node 2's neighbors
5. Pop (2, 2, 1): Add [2, 1], visited: {0, 2, 1}
6. Pop (1, 1, 3): Add [1, 3], visited: {0, 2, 1, 3}
7. All nodes visited, MST complete!

### Example 2: Larger Graph (5 nodes)
```
Graph with 5 nodes and multiple connections
Starting from node 0

Output (MST):
[[0, 1], [1, 2], [0, 3], [1, 4]]

Total Weight: 2 + 3 + 6 + 5 = 16
```

---

## Comparison with Other Algorithms

| Algorithm | Time Complexity | Best For | MST? |
|-----------|-----------------|----------|------|
| **Prim's** | O(E log V) | Dense graphs | ✅ Yes |
| **Kruskal's** | O(E log E) | Sparse graphs | ✅ Yes |
| **Borůvka's** | O(E log V) | Parallel processing | ✅ Yes |
| **Dijkstra's** | O((V+E) log V) | Shortest path (not MST) | ❌ No |

### Prim's vs Kruskal's:

| Aspect | Prim's | Kruskal's |
|--------|--------|-----------|
| **Approach** | Start from a vertex | Sort all edges |
| **Data Structure** | Min-heap, Visited set | Disjoint Set Union |
| **Dense Graphs** | Better (O(E log V)) | Worse |
| **Sparse Graphs** | Worse | Better (O(E log E)) |
| **Edge Sorting** | Not needed | Required |
| **Implementation** | Simpler | Slightly complex |

---

## Key Differences from Dijkstra's

| Feature | Dijkstra's | Prim's |
|---------|-----------|--------|
| **Finds** | Shortest path to all nodes | Minimum spanning tree |
| **Output** | Distances from source | Edges in MST |
| **Graph Type** | Directed/Undirected | Undirected only |
| **Negative Weights** | ❌ Not allowed | ❌ Not allowed |
| **Starting Point** | Fixed source node | Any node works |

---

## Properties of Minimum Spanning Tree

- **V-1 edges**: An MST of V vertices has exactly V-1 edges
- **Connected**: The MST connects all V vertices
- **Acyclic**: The MST contains no cycles
- **Minimum Total Weight**: Sum of edge weights is minimal among all spanning trees
- **Not Unique**: Multiple MSTs can exist with same total weight

---

## Key Takeaways

✨ **Remember:**
1. Prim's finds the **Minimum Spanning Tree** in **O(E log V)** time
2. It works optimally with **non-negative edge weights**
3. It uses a **greedy approach** with a min-heap for efficiency
4. Best suited for **dense graphs**
5. Always adds the **smallest edge** connecting visited to unvisited nodes
6. The MST has exactly **V-1 edges** for V vertices
7. Real-world applications: networks, utilities, infrastructure design

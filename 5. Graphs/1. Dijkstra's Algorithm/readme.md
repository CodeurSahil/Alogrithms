# Dijkstra's Algorithm

## What is Dijkstra's Algorithm?

Dijkstra's Algorithm is a **greedy algorithm** that finds the shortest path between nodes in a weighted graph. It computes the shortest distance from a source node to all other nodes in the graph.

---

## Why Do We Need It?

Dijkstra's algorithm is essential for solving **shortest path problems** in real-world applications:

- **Navigation Systems**: GPS apps (Google Maps, Waze) use Dijkstra's to find the shortest/fastest route between locations
- **Network Routing**: Internet packets use routing algorithms based on Dijkstra's principle to find optimal paths
- **Game Development**: Pathfinding for AI characters and NPCs
- **Telecommunications**: Finding the most efficient data transmission routes
- **Social Networks**: Degrees of separation between users
- **Robot Navigation**: Finding optimal paths for autonomous robots

---

## How It Works

### Algorithm Steps:

1. **Initialize**: 
   - Set distance to source node as 0
   - Set distance to all other nodes as infinity
   - Create a min-heap and add the source node

2. **Iterate**:
   - Extract the node with minimum distance from the heap
   - For each neighbor of the current node:
     - Calculate the tentative distance (current distance + edge weight)
     - If this distance is less than the known distance, update it
     - Add the neighbor to the min-heap

3. **Terminate**: When the heap is empty, all shortest distances are finalized

### Key Principle:
- Always process the node with the **smallest known distance first** (greedy choice)
- This guarantees that once a node is processed, its shortest distance won't change

---

## Complexity Analysis

### Time Complexity: **O((V + E) log V)**

Where:
- **V** = number of vertices (nodes)
- **E** = number of edges

Breaking it down:
- We process each vertex once: **O(V)**
- We process each edge once: **O(E)**
- Each heap operation (push/pop) takes: **O(log V)**
- Total: **O((V + E) log V)**

**Note**: With a Fibonacci heap, this can be optimized to **O(V log V + E)**, but it's rarely used in practice.

### Space Complexity: **O(V)**

- `adj` dictionary storing adjacency list: **O(V + E)**
- `shortest` dictionary storing final distances: **O(V)**
- Min-heap in worst case: **O(V)**
- **Total: O(V + E)** for graph storage + **O(V)** for algorithm = **O(V + E)**

---

## Prerequisites & Constraints

### ✅ When Dijkstra's Works:
- **All edge weights must be non-negative**
- Graphs can be directed or undirected
- Works with weighted graphs

### ❌ When Dijkstra's Doesn't Work:
- **Negative edge weights** → Use Bellman-Ford instead
- **Negative cycles** → Use Bellman-Ford instead

---

## Implementation Details

### Data Structures Used:
1. **Dictionary (adj)**: Stores the graph as an adjacency list
2. **Dictionary (shortest)**: Stores finalized shortest distances
3. **Min-Heap**: Maintains nodes by their distance for efficient extraction of minimum

### Algorithm Advantages:
- ✅ Efficient and optimal for non-negative weights
- ✅ Finds shortest distances to ALL nodes in one pass
- ✅ Greedy approach is intuitive and proven optimal
- ✅ No need to recalculate if you need distances to multiple destinations

### Limitations:
- ❌ Doesn't work with negative edge weights
- ❌ More complex than BFS for unweighted graphs
- ❌ Requires O(V) space for tracking distances

---

## Use Cases & Examples

### Real-World Applications:
1. **GPS Navigation**: Finding shortest driving/walking routes
2. **Network Protocols** (OSPF): Routing packets through networks
3. **Social Media**: Finding closest connections between users
4. **Robotics**: Path planning for autonomous systems
5. **Flight Networks**: Finding cheapest/shortest flight routes

### Problems to Solve:
- Find shortest path from source to one destination
- Find shortest path from source to all destinations
- Find all shortest paths in a network
- Minimum spanning tree variants

---

## Example Walkthrough

### Example 1: Simple Graph
```
Graph:
0 → 1 (weight 4), 0 → 2 (weight 1)
2 → 1 (weight 2)
1 → 3 (weight 1)
2 → 3 (weight 5)

Source: 0, Nodes: 4

Dijkstra's Output: {0: 0, 1: 3, 2: 1, 3: 3}
```

**Shortest paths from node 0:**
- To node 0: 0 (itself)
- To node 1: 3 (via 0→2→1)
- To node 2: 1 (direct)
- To node 3: 3 (via 0→2→1→3)

### Example 2: Complex Graph
```
Graph with 5 nodes and multiple connections
Source: 0, Nodes: 5

Output: {0: 0, 1: 5, 2: 8, 3: 11, 4: 20}
```

---

## Comparison with Other Algorithms

| Algorithm | Time Complexity | Handles Negative Weights | Use Case |
|-----------|-----------------|-------------------------|----------|
| **Dijkstra's** | O((V+E) log V) | ❌ No | Shortest path, non-negative weights |
| **Bellman-Ford** | O(VE) | ✅ Yes | Shortest path, negative weights allowed |
| **Floyd-Warshall** | O(V³) | ✅ Yes | All-pairs shortest paths |
| **BFS** | O(V+E) | - | Unweighted graphs |

---

## Key Takeaways

✨ **Remember:**
1. Dijkstra's finds the shortest path in **O((V+E) log V)** time
2. It works optimally only with **non-negative edge weights**
3. It uses a **greedy approach** with a min-heap for efficiency
4. Once a node is processed, its shortest distance is **finalized**
5. It's the algorithm behind real-world navigation systems

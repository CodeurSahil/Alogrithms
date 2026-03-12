# Topological Sort Algorithm

## What is Topological Sort?

Topological Sort is a **linear ordering of vertices** in a **Directed Acyclic Graph (DAG)** such that for every directed edge (u, v), vertex u comes before vertex v in the ordering. It's only applicable to DAGs (graphs without cycles).

---

## Why Do We Need It?

Topological sorting is essential for solving **dependency and sequencing problems** in real-world applications:

- **Task Scheduling**: Determining order to execute tasks with dependencies (project management)
- **Course Prerequisites**: Ordering courses such that prerequisites are taken first
- **Build Systems**: Compiling source files in correct dependency order
- **Package Management**: Installing software packages in correct dependency order
- **Compiler Design**: Detecting circular dependencies and proper code compilation order
- **Data Processing Pipelines**: Ordering data transformation steps
- **Recipe/Workflow Execution**: Cooking recipes or manufacturing workflows with steps
- **Deadlock Detection**: Identifying circular wait conditions in systems

---

## How It Works

### Algorithm Steps (DFS Approach):

1. **Initialize**:
   - Create an adjacency list representation of the graph
   - Create a visited set and result stack

2. **DFS for Each Node**:
   - For each unvisited node:
     - Perform DFS starting from that node
     - Mark nodes as visited during traversal
     - Add node to result stack **after** visiting all descendants

3. **Reverse Result**:
   - Reverse the stack to get the topological order

### Key Principle:
- A node is added to the result **after** all its descendants are processed
- Reversing gives us the ordering where all dependencies come before dependents

### DFS-Based Topological Sort Pseudocode:
```
function topologicalSort(graph):
    visited = set()
    result = []
    
    for each node in graph:
        if node not in visited:
            dfs(node, visited, result)
    
    return reverse(result)

function dfs(node, visited, result):
    if node in visited:
        return
    
    visited.add(node)
    
    for each neighbor of node:
        dfs(neighbor, visited, result)
    
    result.append(node)  # Add after visiting all descendants
```

---

## Complexity Analysis

### Time Complexity: **O(V + E)**

Where:
- **V** = number of vertices (nodes)
- **E** = number of edges

Breaking it down:
- DFS visits each vertex once: **O(V)**
- DFS traverses each edge once: **O(E)**
- Reversing the result: **O(V)**
- Total: **O(V + E + V) = O(V + E)**

### Space Complexity: **O(V + E)**

- `adj` dictionary (adjacency list): **O(V + E)**
- `visited` set: **O(V)**
- `topo` list (result): **O(V)**
- Recursion call stack (worst case): **O(V)** (path-like graph)
- **Total: O(V + E)**

---

## Prerequisites & Constraints

### ✅ When Topological Sort Works:
- **Directed Acyclic Graph (DAG)** - MUST be acyclic
- Multiple valid topological orderings can exist
- Works with weighted or unweighted edges
- Multiple components are allowed

### ❌ When Topological Sort Doesn't Work:
- **Graphs with cycles** - Result is undefined/meaningless
- **Undirected graphs** - Concept doesn't apply (no direction)
- **Cyclic dependencies** - Indicates impossible scheduling

---

## Cycle Detection

### How to Detect Cycles:

If a graph has a cycle, any topological sort algorithm will fail. You can detect cycles by:

1. **During DFS**: Track nodes in current recursion stack
   ```
   if node in current_stack:
       # Cycle detected!
   ```

2. **Count Edges in Result**: If result has fewer than V nodes, cycle exists

3. **Kahn's Algorithm**: If queue becomes empty before processing all nodes

---

## Implementation Details

### Data Structures Used:
1. **Dictionary (adj)**: Adjacency list storing the graph
2. **Set (visited)**: Tracks which nodes have been visited
3. **List (topo)**: Stores the topological order (built in reverse)

### Algorithm Advantages:
- ✅ DAG verification (if cycle detected, graph is not DAG)
- ✅ Multiple valid orderings exist (algorithm finds one)
- ✅ Efficient linear-time solution
- ✅ Works for disconnected components
- ✅ Can be used for cycle detection

### Limitations:
- ❌ Only works on DAGs (directed acyclic graphs)
- ❌ Doesn't work on cyclic graphs
- ❌ No shortest/longest path information
- ❌ Result can be non-unique (multiple orderings possible)

---

## Use Cases & Examples

### Real-World Applications:
1. **Project Management**: PERT/CPM charts for task scheduling with dependencies
2. **Software Build Systems**: Make, Maven, Gradle compile dependencies in order
3. **Package Managers**: npm, pip determine installation order
4. **University Registration**: Course scheduling respecting prerequisites
5. **Data Processing Pipelines**: ETL workflows with dependent stages
6. **Compiler Design**: Symbol resolution and code generation order
7. **Recipe/Laboratory Procedures**: Step-by-step execution with process sequences
8. **Manufacturing**: Assembly line sequencing with dependencies

### Problems to Solve:
- Detect if a set of tasks can be scheduled (no cycles)
- Find a valid ordering of dependent tasks
- Verify compilation/compilation order
- Check for circular dependencies in software

---

## Example Walkthrough

### Example 1: Course Prerequisites (4 courses)
```
Graph:
0 → 1 (Course 0 prerequisite for Course 1)
0 → 2 (Course 0 prerequisite for Course 2)
1 → 3 (Course 1 prerequisite for Course 3)
2 → 3 (Course 2 prerequisite for Course 3)

DFS Execution from main.py:
1. DFS(0): visits 0 → 1 → 3 → (back) → 2 → 3 (skip, visited)
2. Adds nodes in order: 3, 1, 2, 0
3. Reverses result: [0, 2, 1, 3]

Output: [0, 2, 1, 3]  (or any valid topological order)

Interpretation:
- Course 0 first
- Then Course 2 (or Course 1)
- Then Course 1 (or Course 2)
- Finally Course 3

Valid Ordering: 0 → 2 → 1 → 3 ✓
Valid Ordering: 0 → 1 → 2 → 3 ✓ (Another valid order)
```

**DFS Trace:**
```
Visit 0:
  Visit 1:
    Visit 3: (no neighbors)
      Add 3 to result
    Add 1 to result
  Visit 2:
    Visit 3: (skip, already visited)
    Add 2 to result
  Add 0 to result

Result before reverse: [3, 1, 2, 0]
Result after reverse: [0, 2, 1, 3]
```

### Example 2: Build Dependencies
```
Graph:
main.o depends on helper.o, utils.o
helper.o depends on utils.o
utils.o has no dependencies

Edges:
(0, 1): main depends on helper
(0, 2): main depends on utils
(1, 2): helper depends on utils

Topological Order: 
Build order: [2, 1, 0]
Meaning: Build utils → helper → main
```

---

## Topological Sort vs Other Algorithms

| Algorithm | Type | Time | Use Case |
|-----------|------|------|----------|
| **Topological Sort** | Graph ordering | O(V+E) | Task scheduling, dependencies |
| **DFS** | Graph traversal | O(V+E) | Connectivity, cycles |
| **BFS** | Graph traversal | O(V+E) | Shortest path (unweighted) |
| **Dijkstra's** | Shortest path | O((V+E)logV) | Shortest path (weighted) |
| **Kruskal's** | MST | O(E log E) | Minimum spanning tree |

---

## Properties of Topological Sort

- **Uniqueness**: Not unique - multiple valid orderings can exist
- **Existence**: Only exists for DAGs (Directed Acyclic Graphs)
- **Linear Time**: Always O(V + E) for any graph
- **Edge Direction**: Every edge goes from earlier to later vertex
- **Multiple Roots**: Can have multiple nodes with in-degree 0

---

## Cycle Detection in Directed Graphs

### Using Topological Sort:
```python
def hasCycle(edges, n):
    topo = topologicalSort(edges, n)
    return len(topo) != n  # If fewer nodes, cycle exists
```

### Enhanced DFS with Cycle Detection:
```python
def dfsWithCycleDetection(adj, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)
    
    for neighbor in adj[node]:
        if neighbor not in visited:
            if dfsWithCycleDetection(adj, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True  # Back edge found = cycle
    
    rec_stack.remove(node)
    return False
```

---

## Common Mistakes & Tips

### ❌ Common Mistakes:
1. Applying to graphs with cycles (result is undefined)
2. Forgetting to reverse DFS result
3. Not marking all nodes as visited
4. Confusing topological order with numerical order

### ✅ Tips:
1. Always verify the graph is a DAG first
2. Check all nodes in reversed result are included
3. Verify edge direction in final ordering
4. Multiple valid answers are acceptable
5. Use for dependency resolution and sequencing

---

## Applications in Practice

### 1. **Package Dependencies**
```
Package A depends on B, C
Package B depends on D
Package C depends on D

Install order: D → B, C → A
```

### 2. **Course Prerequisites**
```
Algorithms requires Data Structures
Data Structures requires Programming Basics
Advanced Algorithms requires Algorithms

Take: Programming Basics → Data Structures → 
      Algorithms → Advanced Algorithms
```

### 3. **Build Order**
```
main.cpp depends on helper.h, utils.h
helper.h depends on utils.h

Compile: utils.o → helper.o → main.o
```

---

## Key Takeaways

✨ **Remember:**
1. Topological Sort orders DAG vertices such that all edges go from earlier to later vertices
2. **O(V + E)** time complexity makes it efficient
3. **DFS approach**: Adds nodes after processing descendants, requires reversal
4. **Kahn's approach**: Uses in-degree reduction, no reversal needed
5. Only works on **Directed Acyclic Graphs (DAGs)**
6. **Not unique**: Multiple valid topological orderings can exist
7. Essential for: task scheduling, dependency resolution, compiler design
8. Can detect cycles: if result has fewer than V nodes
9. Real-world uses: build systems, package managers, course scheduling
10. Time complexity matches graph traversal algorithms (DFS/BFS)

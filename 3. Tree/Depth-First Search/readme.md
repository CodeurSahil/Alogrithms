## 📈 Depth-First Search (DFS)

**Depth-First Search (DFS)** is a fundamental algorithm for traversing a tree. The name "depth-first" perfectly describes its strategy: it explores as far down one branch as possible before "backtracking" to explore other branches.

Think of it like navigating a maze. You take the first path you see. You keep walking down that path, taking the first turn at every junction, until you hit a dead end (a leaf node). Only then do you backtrack to the last junction you were at and try the *next* available path.

In the context of trees, DFS isn't a single algorithm but a family of traversals. The three main types—**Pre-order**, **In-order**, and **Post-order**—are all forms of DFS.

-----

## ⚙️ The Algorithm (The Three Traversals)

The "algorithm" for DFS is defined by *when* you "process" the current node (e.t., print its value, add it to a list) relative to its children.

Let's use a binary tree as the standard example, with `Node (N)`, `Left Child (L)`, and `Right Child (R)`.

### 1\. Pre-order Traversal (N-L-R)

This is the most direct implementation of the "visit, then explore" idea.

1.  **Process** the **Node (N)**.
2.  Recursively call DFS on the **Left** child.
3.  Recursively call DFS on the **Right** child.

**Use:** Great for creating a copy of a tree or serializing it, as it saves the root first.

### 2\. In-order Traversal (L-N-R)

This is most often used with Binary Search Trees (BSTs).

1.  Recursively call DFS on the **Left** child.
2.  **Process** the **Node (N)**.
3.  Recursively call DFS on the **Right** child.

**Use:** In a BST, this traversal visits all nodes in **ascending sorted order**.

### 3\. Post-order Traversal (L-R-N)

This "children-first" approach is used when you must process children before the parent.

1.  Recursively call DFS on the **Left** child.
2.  Recursively call DFS on the **Right** child.
3.  **Process** the **Node (N)**.

**Use:** Perfect for deleting a tree. You delete the children *before* you delete the parent.

-----
## 🎯 Where to Use

Use DFS when you need to:

  * **Explore a full path:** Find a path from the root to a leaf that satisfies a condition (e.g., "find a path that sums to 20").
  * **Backtracking:** DFS is the natural engine for all backtracking problems (e.g., pathfinding, solving mazes, Sudoku).
  * **Find *a* solution:** When you just need to find *if* a node exists or *a* path exists, and you don't care if it's the "shortest" one.
  * **Process children before parents:** Use Post-order for tasks like deleting a tree.
  * **Process parents before children:** Use Pre-order for tasks like serializing a tree.

-----

## 🔑 Key Properties

  * **Underlying Data Structure:** DFS uses a **Stack**.
      * In the **recursive** implementation (like the code above), this is the "call stack" managed by the programming language.
      * In an **iterative** implementation, you would create and manage an explicit `Stack` data structure.
  * **Pathing:** It completes one full "branch" of the tree (down to its leaves) before moving to the next sibling branch.
  * **Memory Usage:** The memory used is proportional to the **height** of the tree to store the stack.

-----

## 👍 Advantages

  * **Simple Implementation:** The recursive implementation is often just a few lines of code and is very elegant.
  * **Space Efficient (for wide trees):** If a tree is very "bushy" (wide) but not very "deep," DFS uses far less memory than BFS. The stack only stores the nodes on the current path from the root, not all nodes at a given level.
  * **Finds Deep Solutions:** If the answer you're looking for is deep in the tree, DFS will likely find it faster than BFS.
  * **Natural for Backtracking:** It's the perfect choice for problems where you must make a choice, explore the consequences, and then "un-make" the choice (backtrack) if it doesn't work out.

-----

## 👎 Disadvantages

  * **Stack Overflow:** If the tree is extremely **deep** (e.g., a "skewed" tree that is just a linked list), the recursion can go too deep, causing a stack overflow.
  * **Not for Shortest Paths:** DFS is **not** the algorithm for finding the shortest path from the root to a node. It will find *a* path, but it might be a very long and winding one. (Use **Breadth-First Search (BFS)** for shortest paths).
  * **"Slower" for Shallow Solutions:** If the answer is near the root, DFS may explore an entire, very deep, wrong branch before ever finding it.

-----

## 💡 Applications

  * **Pathfinding:** Finding if a path exists between two nodes.
  * **Path Sum:** Finding a root-to-leaf path that sums to a specific target number.
  * **Tree Traversals (as an application):**
      * **In-order:** Used to get a sorted list of values from a Binary Search Tree (BST).
      * **Post-order:** Used to delete a tree from the bottom up, avoiding "orphaned" nodes.
      * **Pre-order:** Used to copy or serialize a tree so it can be perfectly reconstructed.
  * **Backtracking Problems:** Virtually all backtracking problems on a tree (like finding all root-to-leaf paths) are solved with DFS.

-----

## 📊 Time Complexity Summary

| Component | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time** | **$O(N)$** | You must visit every single node in the tree exactly once. ($N$ is the number of nodes). |
| **Space** | **$O(H)$** | The space used is the maximum size of the (call) stack, which is equal to the **height ($H$)** of the tree. |
| | **Best Case (Space):** $O(\log N)$ | This occurs if the tree is **balanced**. The height of a balanced tree is $\log N$. |
| | **Worst Case (Space):** $O(N)$ | This occurs if the tree is **unbalanced** (skewed), e.g., a linked list. The height is $N$. |

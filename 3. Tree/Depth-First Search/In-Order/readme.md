## 📈 In-order Traversal

**In-order Traversal** is a fundamental traversing algorithm for a tree. It is a type of **Depth-First Search (DFS)**, meaning it explores as far down one branch as possible before backtracking.

The name "In-order" perfectly describes its logic: you **process the node *in between*** processing its left and right children. The simple mnemonic for this traversal is **Left-Node-Right (L-N-R)**.

This traversal is most famous for its special property with **Binary Search Trees (BSTs)**: an in-order traversal of a BST will visit all nodes in their **ascending sorted order**.

-----

## ⚙️ The Algorithm (Recursive vs. Iterative)

The L-N-R logic can be implemented in two main ways:

### 1\. Recursive Algorithm

The recursive approach is the most intuitive and directly follows the L-N-R logic. It is elegant and uses the call stack to handle the "backtracking."

**Algorithm:**

1.  **Base Case:** If the current node is `null`, return.
2.  **Go Left (L):** Recursively call the in-order function on the node's **left** child.
3.  **Process Node (N):** "Visit" the current node (e.g., print its value, add it to a list).
4.  **Go Right (R):** Recursively call the in-order function on the node's **right** child.

-----

### 2\. Iterative Algorithm (Using a Stack)

The iterative approach is less intuitive but avoids recursion limits. It uses an explicit **Stack** to simulate the call stack. The logic is to "go as far left as possible," then process, then go right.

**Algorithm:**

1.  Create an empty **Stack**.
2.  Create a `current` pointer and initialize it to `root`.
3.  Start a master `while` loop that continues as long as `current` is not `null` **OR** the `stack` is not empty.
4.  **Go Left (L):** Inside the loop, have another `while` loop that runs as long as `current` is not `null`:
      * Push `current` onto the stack.
      * Move `current` to `current.left`.
5.  **Process Node (N):** Once the inner loop breaks (`current` is `null`), you've hit the leftmost point.
      * Pop the top node from the stack (this is the node to process).
      * "Visit" the popped node.
6.  **Go Right (R):** Set `current` to the popped node's **right** child.
7.  The master loop repeats, taking this new `current` node and finding *its* leftmost child.

-----

## 🎯 Where to Use

Use In-order Traversal almost any time you are working with a **Binary Search Tree (BST)**.

  * It's the standard way to get all values from a BST in sorted order.
  * It's used to verify if a tree *is* a valid BST (by checking if the output is sorted).

-----

## 🔑 Key Properties

  * It's a **Depth-First Search (DFS)**.
  * In a **Binary Search Tree (BST)**, this traversal visits all nodes in **ascending sorted order**. This is its most important property.
  * The first node processed is the **leftmost** node (the "smallest" in a BST).
  * The last node processed is the **rightmost** node (the "largest" in a BST).

-----

## 👍 Advantages

  * **BST Sorting:** This is its main advantage. It provides a simple, efficient way to flatten a BST into a sorted list.
  * **Simple Logic (Recursive):** The recursive version is very elegant and easy to remember.

-----

## 👎 Disadvantages

  * **Complex Iterative Logic:** The iterative version is the most complex of the three DFS traversals (Pre-order, In-order, Post-order).
  * **Stack Overflow:** The recursive version can cause a "stack overflow" error if the tree is very deep (skewed).
  * **Not for all problems:** It's not the correct choice for copying a tree (use Pre-order) or deleting a tree (use Post-order).

-----

## 💡 Applications

1.  **Validating a BST:** Perform an in-order traversal and store the visited nodes in a list. Check if the list is sorted.
2.  **Flattening a BST:** Perform an in-order traversal to create a sorted list or linked list from a BST.
3.  **Finding k-th Smallest Element in a BST:** Perform an in-order traversal and stop after you have visited `k` nodes.
4.  **Expression Trees:** For a tree representing a mathematical formula, an in-order traversal (with added parentheses) gives you the standard "infix" notation (e.g., `(2 * 3) + 4`).

-----

## 📊 Time Complexity Summary

| Component | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time** | **$O(N)$** | You must visit every single node in the tree exactly once. ($N$ = number of nodes). |
| **Space** | **$O(H)$** | The space is determined by the maximum size of the stack (either the call stack or the iterative one), which is equal to the **height ($H$)** of the tree. |
| | **Best Case (Space):** $O(\log N)$ | This occurs if the tree is **balanced**. |
| | **Worst Case (Space):** $O(N)$ | This occurs if the tree is **unbalanced** (skewed into a linked list). |
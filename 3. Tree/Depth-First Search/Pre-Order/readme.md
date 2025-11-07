## 📈 Pre-order Traversal

**Pre-order Traversal** is a fundamental traversing algorithm for a tree. It is a type of **Depth-First Search (DFS)**, meaning it explores as far down one branch as possible before backtracking.

The name "Pre-order" perfectly describes its logic: you **process the node *before*** you process any of its children. The simple mnemonic for this traversal is **Node-Left-Right (N-L-R)**.

Think of it as a manager giving an order:

1.  The manager (Node) first gives the order (processes their value).
2.  Then, they pass the order to their left-hand subordinate (Left child).
3.  Finally, they pass the order to their right-hand subordinate (Right child).

-----

## ⚙️ The Algorithm (Recursive vs. Iterative)

The N-L-R logic can be implemented in two main ways:

### 1\. Recursive Algorithm

The recursive approach is the most intuitive and directly follows the N-L-R logic. It uses the call stack to handle the "backtracking."

**Algorithm:**

1.  **Base Case:** If the current node is `null`, return.
2.  **Process Node (N):** "Visit" the current node (e.g., print its value, add it to a list).
3.  **Go Left (L):** Recursively call the pre-order function on the node's **left** child.
4.  **Go Right (R):** Recursively call the pre-order function on the node's **right** child.

-----

### 2\. Iterative Algorithm (Using a Stack)

The iterative approach mimics the recursive call stack using an explicit **Stack** data structure. It's a bit less intuitive but avoids recursion limits.

**Algorithm:**

1.  Create an empty **Stack**.
2.  If the `root` is `null`, return.
3.  Push the `root` node onto the Stack.
4.  Loop while the Stack is **not** empty:
    1.  **Pop** a node from the Stack (let's call it `current`).
    2.  **Process `current` (N):** Visit the `current` node.
    3.  **Push `Right` Child (R):** Push the `current` node's **right** child onto the Stack (if it exists).
    4.  **Push `Left` Child (L):** Push the `current` node's **left** child onto the Stack (if it exists).

> **Important:** You must push the **right** child *before* the **left** child. Because a stack is **Last-In, First-Out (LIFO)**, pushing `left` last ensures it will be the *first* one popped and processed, correctly maintaining the N-L-R order.

-----

## 🎯 Where to Use

Use Pre-order Traversal when you need to process a parent node *before* you process its children.

  * It's ideal for **copying** a tree. You create the new parent node *before* you recurse to create its children.
  * It's used when you need to **serialize** a tree (save its structure to a file or string), as it's easy to reconstruct from this order (especially with `null` markers).

-----

## 🔑 Key Properties

  * It's a **Depth-First Search (DFS)**.
  * The very **first node** processed is always the **root** of the tree.
  * In any subtree, the root of that subtree is always visited before any of its descendants.

-----

## 👍 Advantages

  * **Simplicity:** The recursive version is extremely simple and elegant.
  * **Copying:** It's the most natural traversal for creating a structural copy of a tree.
  * **Iterative Simplicity:** The iterative version is simpler than the iterative versions for In-order or Post-order.

-----

## 👎 Disadvantages

  * **Stack Overflow:** The recursive version can cause a "stack overflow" error if the tree is very deep (e.g., a "skewed" tree that acts like a linked list).
  * **Not for All Problems:** It's not the right tool for every job. For example, you **cannot** use it to delete a tree (you would delete the parent before its children).

-----

## 💡 Applications

1.  **Copying a Tree:** This is the most common application. You create the new node (N), then recursively call the copy function for its left (L) and right (R) children.
2.  **Serialization:** Storing a tree's structure to a file or string.
3.  **Prefix Expressions (Polish Notation):** If a tree represents a mathematical expression, a pre-order traversal will give you the prefix form (e.g., `+ * 2 3 4` instead of `(2 * 3) + 4`).

-----

## 📊 Time Complexity Summary

| Component | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time** | **$O(N)$** | You must visit every single node in the tree exactly once. ($N$ = number of nodes). |
| **Space** | **$O(H)$** | The space is determined by the maximum size of the stack (either the call stack or the iterative one), which is equal to the **height ($H$)** of the tree. |
| | **Best Case (Space):** $O(\log N)$ | This occurs if the tree is **balanced**. |
| | **Worst Case (Space):** $O(N)$ | This occurs if the tree is **unbalanced** (skewed into a linked list). |
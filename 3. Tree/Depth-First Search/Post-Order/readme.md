## 📈 Post-order Traversal

**Post-order Traversal** is a fundamental traversing algorithm for a tree. It is a type of **Depth-First Search (DFS)**, meaning it explores as far down one branch as possible before backtracking.

The name "Post-order" means you **process the node *after*** you have processed all of its children. The simple mnemonic for this traversal is **Left-Right-Node (L-R-N)**.

Think of it as a "bottom-up" approach. You must completely finish all work in the left and right subtrees before you can finally process the parent node. This makes it perfect for tasks like deleting a tree: you must delete the children (L and R) before you can safely delete the parent (N).

-----

## ⚙️ The Algorithm (Recursive vs. Iterative)

The L-R-N logic can be implemented in two main ways. The iterative version is notably more complex than it is for Pre-order or In-order.

### 1\. Recursive Algorithm

The recursive approach is the most intuitive and directly follows the L-R-N logic. It is simple, elegant, and uses the call stack to handle backtracking.

**Algorithm:**

1.  **Base Case:** If the current node is `null`, return.
2.  **Go Left (L):** Recursively call the post-order function on the node's **left** child.
3.  **Go Right (R):** Recursively call the post-order function on the node's **right** child.
4.  **Process Node (N):** "Visit" the current node (e.g., print its value, add it to a list).

-----

### 2\. Iterative Algorithm (Using 2 Stacks)

The iterative post-order is the trickiest of the three traversals. The simplest and most common iterative solution cleverly uses two stacks (or one stack and a result list) to reverse a modified Pre-order traversal.

**Algorithm (Two Stacks):**

1.  Create two empty stacks, `stack1` and `stack2`.
2.  Push the `root` node onto `stack1`.
3.  Loop while `stack1` is **not** empty:
    1.  Pop a node from `stack1` (let's call it `current`).
    2.  Push `current` onto `stack2`.
    3.  Push `current`'s **left** child onto `stack1` (if it exists).
    4.  Push `current`'s **right** child onto `stack1` (if it exists).
4.  After the loop, `stack1` is empty. Now, pop every node from `stack2` and process it. The order will be perfect Post-order (L-R-N).

**Why this works:** The loop on `stack1` processes nodes in a **N-R-L** (Node-Right-Left) order. `stack2`'s only job is to store these popped nodes, effectively reversing this `N-R-L` order into **L-R-N**.


-----

## 🎯 Where to Use

Use Post-order Traversal when you **must** process or operate on the children *before* you can process the parent.

  * It's essential for any "bottom-up" logic.
  * It's used when the value of a parent node depends on the values of its children.

-----

## 🔑 Key Properties

  * It's a **Depth-First Search (DFS)**.
  * The very **last node** processed is always the **root** of the tree.
  * In any subtree, the root of that subtree is always visited after all of its descendants.

-----

## 👍 Advantages

  * **Deletion:** It's the only traversal that allows you to safely delete all nodes in a tree.
  * **Expression Evaluation:** It's the "natural" way to evaluate an expression tree.
  * **Dependency Resolution:** It ensures all "child" dependencies are handled before the "parent" task.

-----

## 👎 Disadvantages

  * **Complex Iterative Logic:** The iterative version is the most complex of the three DFS traversals, often requiring two stacks or a clever reversal.
  * **Stack Overflow:** The recursive version (like all recursive DFS) can cause a "stack overflow" error if the tree is very deep (skewed).

-----

## 💡 Applications

1.  **Deleting a Tree:** This is the most famous application. You must delete the left and right children before you can delete (and free the memory for) the parent.
2.  **Evaluating an Expression Tree:** A tree like `+` with children `*` and `4` (where `*` has children `2` and `3`) represents `(2 * 3) + 4`. Post-order (L-R-N) would process:
    1.  `2`
    2.  `3`
    3.  `*` (evaluates to $2 \times 3 = 6$)
    4.  `4`
    5.  `+` (evaluates to $6 + 4 = 10$)
3.  **Finding Dependencies:** In a task graph, this ensures all prerequisite tasks (children) are completed before the main task (parent) is run.

-----

## 📊 Time Complexity Summary

| Component | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time** | **$O(N)$** | You must visit every single node in the tree exactly once. ($N$ = number of nodes). |
| **Space** | **$O(H)$** | The space is determined by the maximum size of the stack(s), which is equal to the **height ($H$)** of the tree. |
| | **Best Case (Space):** $O(\log N)$ | This occurs if the tree is **balanced**. |
| | **Worst Case (Space):** $O(N)$ | This occurs if the tree is **unbalanced** (skewed into a linked list). |x
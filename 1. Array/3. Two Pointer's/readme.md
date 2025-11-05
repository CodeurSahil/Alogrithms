## 📈 Two Pointer

The **Two Pointer** technique is a powerful and efficient algorithmic pattern used to process arrays or lists. It's not a single algorithm but a versatile *strategy* for solving problems.

The core idea is to use two variables (the "pointers"), which are typically array indices or list node iterators. These pointers move through the data, and their positions relative to each other are used to find a solution.

This technique is most famous for its ability to transform a "brute-force" solution with nested loops (often $O(N^2)$ complexity) into a highly optimized single-pass solution (usually **$O(N)$** time).



---

## ⚙️ The Algorithm (The Main Patterns)

There isn't one single "algorithm." The Two Pointer technique is applied in several common patterns.

### Pattern 1: Opposite-Direction Pointers (Converging)

This is the most common pattern, where two pointers start at opposite ends of a **sorted** array and move toward each other.

* **Setup:** `left = 0`, `right = length - 1`
* **Logic:**
    1.  Start a loop that continues as long as `left < right`.
    2.  Check the condition based on `arr[left]` and `arr[right]`.
    3.  **Move the pointers:** Based on the condition, you will move *one* of the pointers to get closer to the desired state.
        * If the sum is too small, you need a larger number, so you move the left pointer: `left++`.
        * If the sum is too large, you need a smaller number, so you move the right pointer: `right--`.
    4.  The loop terminates when `left` and `right` cross.

### Pattern 2: Same-Direction Pointers (Fast/Slow)

In this pattern, both pointers start at or near the beginning of the array and move in the same direction, but at different speeds.

* **Setup:** `left = 0`, `right = 0` (or `slow = 0`, `fast = 0`)
* **Logic:**
    1.  The `right` (or `fast`) pointer expands to explore new elements and find a state that meets a condition.
    2.  The `left` (or `slow`) pointer follows, often to "shrink" the window or mark a new beginning.
    3.  The distance between `left` and `right` forms a "window" that can grow or shrink.

> **Note:** This pattern is the *exact* same technique as the **Variable-Size Sliding Window**. "Sliding Window" is just a more specific name for this two-pointer pattern.

### Pattern 3: Floyd's Tortoise and Hare (Linked Lists)

This is a famous, specific application of the fast/slow pattern, primarily for linked lists.

* **Setup:** `slow = head`, `fast = head`
* **Logic:**
    1.  In each step, move `slow` by one node: `slow = slow.next`.
    2.  Move `fast` by two nodes: `fast = fast.next.next`.
    3.  If `fast` reaches the end (is `null`), there is no cycle.
    4.  If `slow == fast` at any point, a cycle has been detected.

---

## 🎯 Where to Use

Use the Two Pointer technique when:

* You have a **sorted array** and need to find a pair, triplet, or subarray that meets a target value.
* You need to check for a **palindrome** in a string or array.
* You need to process a list and **remove duplicates** or **partition** the data (e.g., move all zeros to the end).
* You need to find the **longest/shortest contiguous subarray** that satisfies a condition (this is the Sliding Window pattern).
* You need to detect a **cycle in a linked list**.
* You need to find the **middle of a linked list**.

---

## 🔑 Key Properties

* **Single Pass:** The solution is almost always achieved in a single pass through the data.
* **In-Place:** The technique often modifies the array "in-place" without needing extra data structures (unless a hash map is used for the sliding window).
* **Stateful Pointers:** The pointers' positions (and the gap between them) represent a specific "state," like the current sum, the current window, or the items being compared.
* **Sorting Prerequisite (Often):** The "Opposite-Direction" pattern *only* works if the data is sorted. If it's not, you must sort it first.

---

## 👍 Advantages

* **Time Efficiency:** This is the main benefit. It reduces time complexity from a naive $O(N^2)$ to **$O(N)$**.
* **Space Efficiency:** It runs in **$O(1)$** constant space (for the pointers themselves). This makes it incredibly memory-efficient.

---

## 👎 Disadvantages

* **Sorting Cost:** If the "Opposite-Direction" pattern is used on unsorted data, the required sorting step adds an **$O(N \log N)$** time cost, which becomes the bottleneck.
* **Not a "Silver Bullet":** It's a pattern, not a data structure. You can't just "use" two-pointers; you must correctly identify *how* to apply the logic (i.e., when to move `left` vs. `right`).
* **Tricky Edge Cases:** Handling the loop condition (`<` vs. `<=`) and pointer initialization can be confusing and lead to "off-by-one" errors.

---

## 💡 Applications

This technique is the foundation for solving many classic problems.

* **Opposite-Direction (Converging):**
    * **Two Sum II:** Given a *sorted* array, find two numbers that add up to a target.
    * **Palindrome Check:** Check if `str[left]` equals `str[right]`.
    * **Reverse an Array/String:** Swap `arr[left]` and `arr[right]` and move both pointers.
* **Same-Direction (Sliding Window):**
    * **Longest Substring Without Repeating Characters:** The `right` pointer expands, and `left` shrinks the window when a repeat is found.
    * **Smallest Subarray with Sum $\ge S$:** (The classic variable-window problem).
    * **Remove Duplicates from Sorted Array:** The `fast` pointer scans, and the `slow` pointer points to the end of the new, unique array.
* **Fast/Slow (Linked Lists):**
    * Linked List Cycle Detection.
    * Find the middle of a Linked List (when `fast` reaches the end, `slow` is at the middle).

---

## 📊 Time Complexity Summary

| Component | Complexity | Explanation |
| :--- | :--- | :--- |
| **Two Pointer Algorithm** | **$O(N)$** | In all patterns, each pointer traverses the list at most once. $O(N + N)$ simplifies to $O(N)$. |
| **If Sorting is Required** | **$O(N \log N)$** | The sort takes $O(N \log N)$, and the two-pointer scan takes $O(N)$. The sort is the bottleneck. |
| **Space Complexity** | **$O(1)$** | The pointers are just a few variables. (This can be $O(k)$ for sliding windows that use a hash map). |

---

## ✨ Other Things You Should Know

### 1. Two Pointers vs. Sliding Window

This is the most common point of confusion.
* **Two Pointer** is the *general technique*.
* **Sliding Window** (both fixed and variable) is a *specific application* of the Two Pointer technique (the "Same-Direction" pattern).

In short: **All Sliding Window algorithms are Two Pointer algorithms, but not all Two Pointer algorithms are Sliding Windows.** (The "Opposite-Direction" pattern is not a sliding window).

### 2. The "Dutch National Flag" Problem

This is a famous advanced two-pointer problem.
* **Problem:** Sort an array of `0`s, `1`s, and `2`s in-place.
* **Solution:** It's an extension of the two-pointer idea, but it uses **three pointers**:
    * `low` starts at `0`.
    * `mid` starts at `0`.
    * `high` starts at `n - 1`.
* You iterate with `mid`. If `arr[mid]` is `0`, you swap it with `arr[low]` and increment both. If it's `2`, you swap it with `arr[high]` and decrement `high`. If it's `1`, you just increment `mid`.
* This is a perfect example of how the core "pointer" concept can be extended.
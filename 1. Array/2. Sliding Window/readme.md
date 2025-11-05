## 📈 Sliding Window

The **Sliding Window** is not a data structure, but a powerful algorithmic **technique** or **pattern**. It is used to efficiently solve problems involving **contiguous** portions of data, such as arrays or strings.

Think of it as a conceptual "window" that slides over the data. This window represents a temporary, contiguous subarray or substring. The technique's power comes from its efficiency: instead of re-calculating everything for each new subarray, it intelligently updates the previous window's result by "sliding" — adding the new element at one end and (often) removing the old element at the other.

This method almost always reduces a naive brute-force $O(N^2)$ or $O(N^3)$ solution down to a highly efficient **$O(N)$** linear time solution.

---

## ⚙️ The Algorithm (The Two Main Patterns)

The "algorithm" for a sliding window depends entirely on the problem. It splits into two  main patterns:

### Pattern 1: [Fixed-Size Window](./Fixed/readme.md)

This is the simplest pattern, used when the problem specifies a **fixed size `k`** for the window.

### Pattern 2: [Variable-Size (Dynamic) Window](./Variable/readme.md)

This is the more advanced pattern, used when the window size is **not fixed**. The problem will ask you to find the **longest** or **shortest** window that satisfies a condition.

---

## 🎯 Where to Use

Use the Sliding Window technique when a problem:
* Involves a **contiguous** subarray, list, or substring.
* Asks for an optimal value (like **max sum**, **min length**, **longest substring**).
* Can be naively solved with nested loops (a $O(N^2)$ brute-force).

**Look for keywords:**
* **Fixed-Size:** "subarray of size `k`," "all permutations of length `k`," "moving average."
* **Variable-Size:** "**longest** subarray," "**shortest** substring," "at most `k` distinct," "sum $\ge X$."

---

## 🔑 Key Properties

* **Contiguous Data:** The technique *only* works on contiguous (adjacent) elements. It cannot be used for "subsequences" (where elements can be skipped).
* **Two Pointers:** At its core, a sliding window is a specific implementation of the **Two Pointer** technique, where the pointers (`left` and `right`) move in the same direction.
* **State Management:** You always need to track the "state" of the current window (e.g., `current_sum`, a hash map of character counts, etc.).
* **$O(N)$ Time (Amortized):** This is the main goal. Each element is processed at most twice (once by the `right` pointer, once by the `left`), so the total time is $O(2N)$, which simplifies to $O(N)$.

---

## 👍 Advantages

* **Massive Efficiency:** It provides a huge performance boost, turning $O(N^2)$ problems into $O(N)$.
* **Low Memory:** It's very space-efficient, typically using $O(1)$ or $O(k)$ space (where $k$ is a constant, like the size of the alphabet). It does *not* use $O(N)$ extra space.
* **Versatile:** The two patterns are templates that can be adapted to solve a wide class of problems.

---

## 👎 Disadvantages

* **Contiguous Only:** It cannot solve problems on non-adjacent data (subsequences).
* **Tricky Logic:** The variable-size window, with its "expand-shrink" `while` loop, can be difficult to implement correctly. Off-by-one errors are common.
* **Negative Numbers:** For variable-size sum problems, negative numbers can break the logic (e.g., shrinking the window by removing a negative number *increases* the sum).

---

## 📊 Time Complexity Summary

| Component | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time** | **$O(N)$** | **Amortized.** The `right` pointer moves $N$ times. The `left` pointer *also* moves at most $N$ times. The total work is $O(N + N) = O(2N)$, which is linear. |
| **Space** | **$O(1)$** or **$O(k)$**| $O(1)$ for simple problems (like sum). $O(k)$ if a hash map is used, where $k$ is the number of possible unique elements (e.g., 26 for the alphabet), **not** $N$. |

---

## ✨ Other Things You Should Know

### 1. Sliding Window is a Two-Pointer Technique
The Sliding Window pattern is a more specific name for the "Same-Direction" or "Fast/Slow" **Two Pointer** strategy. The `left` and `right` pointers of the window are the two pointers.

### 2. The Golden Rule: Fixed vs. Variable
The most important skill is identifying which pattern to use.

* If the problem gives you the size `k` (e.g., "of size `k`"), use the **Fixed-Size** pattern.
* If the size is the *answer* you're looking for (e.g., "**shortest**," "**longest**"), use the **Variable-Size** pattern.

### 3. Combining with Data Structures
The Sliding Window technique is the *engine*, but it often needs a *dashboard* (a data structure) to track the window's state.
* **Hash Map (Dictionary):** The most common. Used to count character frequencies.
* **Set:** Used to check for duplicates (e.g., "longest substring with no repeats").
* **Deque (Double-Ended Queue):** A more advanced use. Used to solve "Sliding Window Maximum," where you need to find the max/min *inside* the window in $O(1)$ time.
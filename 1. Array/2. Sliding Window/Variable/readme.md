## 📈 Sliding Window(Variable-Size)

The **Variable-Size Sliding Window** is an algorithmic technique used to efficiently solve problems that involve finding an optimal (e.g., **longest** or **shortest**) contiguous subarray or substring that satisfies a specific condition.

Unlike its "fixed-size" cousin, the window's length is not given. Instead, the window **grows** and **shrinks** dynamically to find the best possible size.

Think of it as an elastic band. You stretch the band (expand the window) by moving a `right` pointer until your data (the subarray) meets a condition. Then, you "inch" the band forward (shrink the window) by moving a `left` pointer to find the *smallest possible size* that *still* meets that condition, before you start expanding again.

-----

## ⚙️ The Algorithm (Step-by-Step)

The core logic uses two pointers, `left` and `right`, and a "state" (like a `current_sum` or a character count) that tracks the condition.

Let's use a classic problem: **"Find the length of the shortest contiguous subarray whose sum is $\ge S$."**

**Array:** `[2, 3, 1, 2, 4, 3]`
**Target `S`:** `7`

We will need:

  * `left = 0` (the left edge of the window)
  * `right = 0` (the right edge of the window)
  * `current_sum = 0` (the state we are tracking)
  * `min_length = Infinity` (our answer)

<!-- end list -->

1.  **Expand (The `right` pointer):**

      * Move `right` one step at a time, adding the new element to `current_sum`, *until* the condition is met.
      * `right = 0` (val=2): `current_sum = 2`. (2 \< 7. Keep expanding).
      * `right = 1` (val=3): `current_sum = 5`. (5 \< 7. Keep expanding).
      * `right = 2` (val=1): `current_sum = 6`. (6 \< 7. Keep expanding).
      * `right = 3` (val=2): `current_sum = 8`. (8 $\ge$ 7. **Condition met\! Stop expanding.**)

2.  **Record (Update Answer):**

      * Now that the condition is met, we have a *potential* answer.
      * The current window is `[2, 3, 1, 2]`.
      * The length is `right - left + 1` = `3 - 0 + 1 = 4`.
      * `min_length = min(Infinity, 4)` = **4**.

3.  **Shrink (The `left` pointer):**

      * Now, we try to find a *better* (smaller) window.
      * Move `left` one step at a time, subtracting its element from `current_sum`, *while* the condition is *still* met.
      * Subtract `arr[left]` (which is 2): `current_sum = 8 - 2 = 6`.
      * `left` moves to 1.
      * Check condition: Is 6 $\ge$ 7? **No.** The condition is broken. **Stop shrinking.**

4.  **Repeat:**

      * Go back to step 1. The window is `[3, 1, 2]`.
      * **Expand:**
          * `right = 4` (val=4): `current_sum = 6 + 4 = 10`. (10 $\ge$ 7. **Condition met\!**)
      * **Record:**
          * Window is `[3, 1, 2, 4]`.
          * Length is `right - left + 1` = `4 - 1 + 1 = 4`.
          * `min_length = min(4, 4)` = **4**.
      * **Shrink:**
          * Subtract `arr[left]` (which is 3): `current_sum = 10 - 3 = 7`.
          * `left` moves to 2.
          * Check condition: Is 7 $\ge$ 7? **Yes\!**
      * **Record:**
          * Window is `[1, 2, 4]`.
          * Length is `right - left + 1` = `4 - 2 + 1 = 3`.
          * `min_length = min(4, 3)` = **3**.
      * **Shrink:**
          * Subtract `arr[left]` (which is 1): `current_sum = 7 - 1 = 6`.
          * `left` moves to 3.
          * Check condition: Is 6 $\ge$ 7? **No.** Stop shrinking.
      * ...This process continues until `right` reaches the end. The final answer is **3**.

-----

## 🎯 Where to Use

Use the variable-size sliding window pattern when a problem asks for the:

  * **Smallest** / **Shortest** subarray or substring...
  * **Largest** / **Longest** subarray or substring...
  * ...that **satisfies a condition**.

The condition might be:

  * "Has a sum $\ge S$"
  * "Has at most `k` distinct characters"
  * "Contains no repeating characters"
  * "Has a sum equal to `S`" (for positive numbers)

-----

## 🔑 Key Properties

  * **Two Pointers:** Uses a `left` and `right` pointer to define the window.
  * **Dynamic Size:** The window size (`right - left + 1`) is not fixed; it grows and shrinks.
  * **One-Pass (Amortized):** The algorithm achieves its efficiency by processing each element at most twice (once by the `right` pointer, once by the `left` pointer).
  * **Condition-Driven:** The movement of the pointers is controlled by whether a specific condition is met.

-----

## 👍 Advantages

  * **Optimal Efficiency:** It converts a brute-force $O(N^2)$ or $O(N^3)$ problem into a highly efficient **$O(N)$** solution.
  * **Reusable Template:** The basic "expand-shrink" logic is a template that can be adapted to a wide variety of problems.
  * **Low Memory:** It typically uses **$O(1)$** extra space for simple problems (like sum) or $O(k)$ for more complex ones (like "k distinct characters," where $k$ is the size of the alphabet, not $N$).

-----

## 👎 Disadvantages

  * **More Complex Logic:** It's more complex than the fixed-window pattern. The inner `while` loop (the shrink step) can be tricky to get right.
  * **Not for All Problems:** It only works for contiguous subarrays and cannot be used for subsequence problems.
  * **Tricky with Negative Numbers:** This pattern works best when the "condition" is monotonic. For example, in a sum-based problem, it relies on the sum *decreasing* when the `left` pointer moves. If the array has negative numbers, removing a negative number *increases* the sum, which can break the logic.

-----

## 💡 Applications

  * **Smallest subarray with sum $\ge S$:** (The example we used).
  * **Longest substring with at most `k` distinct characters:**
      * Condition: `len(character_map) <= k`
      * Expand `right` as long as the condition is met.
      * If the condition breaks, shrink `left` until it's valid again.
  * **Longest substring with no repeating characters:**
      * This is a special case where `k=1` for each character.
      * Condition: `character_map[char] == 1`
  * **String/Substring Search:** Finding the shortest substring that contains all characters of a pattern.

-----

## 📊 Time Complexity Summary

| Component | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time** | **$O(N)$** | This is **Amortized $O(N)$**. The `right` pointer visits each element once ($O(N)$). The `left` pointer also visits each element at most once ($O(N)$). The total operations are $O(N + N) = O(2N)$, which simplifies to $O(N)$. |
| **Space** | **$O(1)$** or **$O(k)$**| $O(1)$ for simple problems (like sum). $O(k)$ if a hash map is used to track character counts, where $k$ is the number of distinct elements (e.g., 26 for the alphabet). |
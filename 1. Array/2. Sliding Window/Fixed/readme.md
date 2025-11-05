## 📈 Sliding Window(Fixed-Size)

The **Fixed-Size Sliding Window** is a powerful algorithmic technique used to efficiently solve problems that involve analyzing a **contiguous subarray** or **substring** of a fixed length, `k`.

Think of it like moving a `k`-sized window frame across a long list of items. Instead of recalculating everything inside the frame every time you move it one step, you just **add the new item** that's entering the window (on the right) and **remove the old item** that's leaving the window (on the left).

This "slide" operation, which takes constant time, is the key to its efficiency. It avoids redundant calculations and dramatically speeds up the process compared to a brute-force approach.

-----

## ⚙️ The Algorithm (Step-by-Step)

Let's use a classic problem: **"Find the maximum sum of any contiguous subarray of size `k`."**

**Array:** `[1, 3, -1, -3, 5, 3, 6, 7]`
**`k`:** `3`

1.  **Initialize (The First Window):**

      * Create the first "window" by summing the first `k` elements.
      * `1 + 3 + (-1) = 3`
      * Set `current_sum = 3`
      * Set `max_sum = 3`

2.  **Start Sliding:**

      * Begin a loop that starts from the `k`-th element (index `k`) and goes to the end of the array.
      * Our loop starts at index 3 (value `-3`).

3.  **Slide (The Core Logic):**

      * **Window 2 (index `i = 3`):**
          * **Add** the new element entering the window: `current_sum = 3 + (-3) = 0`
          * **Subtract** the element leaving the window: `current_sum = 0 - 1 = -1`
          * (Window is now `[3, -1, -3]`, sum is -1)
          * Compare with `max_sum`: `max(-1, 3)` is 3. `max_sum` remains 3.
      * **Window 3 (index `i = 4`):**
          * **Add** new element (`5`): `current_sum = -1 + 5 = 4`
          * **Subtract** old element (`3`): `current_sum = 4 - 3 = 1`
          * (Window is now `[-1, -3, 5]`, sum is 1)
          * Compare with `max_sum`: `max(1, 3)` is 3. `max_sum` remains 3.
      * **Window 4 (index `i = 5`):**
          * **Add** new element (`3`): `current_sum = 1 + 3 = 4`
          * **Subtract** old element (`-1`): `current_sum = 4 - (-1) = 5`
          * (Window is now `[-3, 5, 3]`, sum is 5)
          * Compare with `max_sum`: `max(5, 3)` is 5. `max_sum` is now 5.
      * ... This continues until the end. The final answer will be 16 (from `[5, 3, 6, 7]`).

-----

## 🎯 Where to Use

Use the fixed-size sliding window pattern when a problem:

  * Involves a **contiguous** subarray, list, or substring.
  * Specifies a **fixed size `k`** for that subarray.
  * Asks for a specific value from that window (max, min, average, sum) or a property of it (e.g., "contains an anagram").

-----

## 🔑 Key Properties

  * **Fixed Window Size:** The length `k` never changes.
  * **One-Pass:** The algorithm iterates through the array just once.
  * **$O(1)$ Slide Operation:** The cost of moving the window one step is constant (one addition and one subtraction), regardless of the window's size.
  * **Contiguous Data:** The technique only works for elements that are adjacent.

-----

## 👍 Advantages

  * **High Efficiency:** It reduces the time complexity from $O(N \times k)$ (a naive approach) to **$O(N)$**. This is a massive performance gain.
  * **Simplicity:** The logic is straightforward and easy to implement once you understand the "add-right, subtract-left" concept.
  * **Low Memory:** It typically uses **$O(1)$** extra space, as you only need to store a few variables (`current_sum`, `max_sum`, etc.).

-----

## 👎 Disadvantages

  * **Fixed Size Only:** This specific technique is not suitable for problems where the window size needs to change (e.g., "find the *smallest* subarray with a sum $\ge S$").
  * **Contiguous Only:** It cannot be used for problems involving non-adjacent elements (i.e., subsequences).

-----

## 💡 Applications

  * **Data Streaming:** Calculating a "moving average" over the last `k` data points in a stream.
  * **Sum/Max/Min Problems:**
      * Find the maximum/minimum sum of all subarrays of size `k`.
      * Find the average of all subarrays of size `k`.
  * **String Problems:**
      * Find all anagrams/permutations of a pattern string within a larger string. (The window size `k` is the length of the pattern).
  * **Array Problems:**
      * Find the first negative number in every window of size `k`.
      * Count distinct elements in every window of size `k`. (Requires a hash map).

-----

## 📊 Time Complexity Summary

| Component | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time** | **$O(N)$** | We process the first window ($O(k)$) and then slide $N-k$ times, with each slide being $O(1)$. Total: $O(k + N - k) = O(N)$. |
| **Space** | **$O(1)$** | For simple problems like `max_sum`. We only store a few variables. (Can be $O(k)$ if a hash map or deque is needed). |

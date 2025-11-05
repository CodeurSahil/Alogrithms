## 📈 Kadane's Algorithm

**Kadane's Algorithm** is a powerful and remarkably simple dynamic programming algorithm. Its purpose is to solve the **"Maximum Subarray Problem"**: finding the contiguous (adjacent) subarray within a one-dimensional array of numbers that has the largest possible sum.

For example, in the array `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`, the contiguous subarray with the largest sum is `[4, -1, 2, 1]`, and its sum is **6**.

The algorithm is famous for its efficiency, solving this problem in a single pass with **$O(n)$ time** and **$O(1)$ space**.

-----

## ⚙️ The Algorithm (Step-by-Step)

The core idea is to iterate through the array and, at each position, determine the maximum sum of a subarray that *ends at that position*.

To do this, we only need two variables:

1.  `current_max`: Stores the maximum sum of a subarray that *ends at the current index*.
2.  `max_so_far`: Stores the maximum sum found *anywhere* in the array so far. This is our final answer.

Here is the step-by-step process:

1.  **Initialize:**

      * Set `current_max` = `arr[0]`
      * Set `max_so_far` = `arr[0]`
        *(This handles cases where the array is all-negative. A common mistake is initializing to 0).*

2.  **Loop:** Iterate through the array starting from the second element (`i = 1`). For each element:

      * **Update `current_max`:** This is the heart of the algorithm. The maximum sum ending at this position `i` is either:
        a) The element `arr[i]` itself (i.e., starting a *new* subarray).
        b) The element `arr[i]` *plus* the previous `current_max` (i.e., *extending* the previous subarray).
          * In code: `current_max = max(arr[i], current_max + arr[i])`
      * **Update `max_so_far`:** After updating `current_max`, check if this new local maximum is the best we've seen *anywhere* in the array.
          * In code: `max_so_far = max(max_so_far, current_max)`

3.  **Finish:** After the loop, `max_so_far` holds the maximum contiguous subarray sum.

-----

## 🔑 Key Properties

  * **Dynamic Programming:** It's a classic DP problem. The solution for the current state (max sum at index `i`) is built directly from the solution for the previous state (max sum at index `i-1`).
  * **One-Pass:** The algorithm only needs to iterate through the array once.
  * **Contiguous:** The problem specifically finds a sum from a *contiguous* block of elements. It will not skip elements.
  * **All-Negative Handling:** The initialization (setting `max_so_far` to `arr[0]`) correctly handles arrays with all negative numbers. The answer for `[-5, -2, -1]` will be `-1`, which is the largest sum.

-----

## 👍 Advantages

  * **Extremely Fast:** It has a linear time complexity of **$O(n)$**, which is the fastest possible as it must look at every element at least once.
  * **Memory Efficient:** It has a constant space complexity of **$O(1)$**. It only uses a couple of variables, regardless of the array's size.
  * **Simple:** The logic is short, elegant, and relatively easy to implement, making it a favorite in technical interviews.

-----

## 👎 Disadvantages

  * **Limited Scope:** It only solves this one specific problem (maximum *contiguous* sum). It cannot be used to find a non-contiguous subarray sum (which is a simpler problem: just sum all positive numbers).
  * **Finds Sum, Not Subarray:** The basic algorithm (shown above) only returns the *sum*. It doesn't tell you the `start` and `end` indices of the subarray that produces this sum. (This can be added with a few extra variables, see below).

-----

## 💡 Applications

  * **Stock Market Analysis:** If an array represents daily stock price *changes* (e.g., `[+10, -5, +3, -8, +12]`), Kadane's algorithm can find the most profitable contiguous period (the one with the maximum sum).
  * **Image Processing:** Can be used to find the brightest/darkest contiguous 1D or 2D area (as a building block for the 2D version) in a pixel-intensity map.
  * **Bioinformatics:** Used in problems like finding high-scoring segments within a protein sequence.
  * **Technical Interviews:** It is one of the most common and fundamental dynamic programming questions.

-----

## 📊 Time Complexity Summary

| Case | Complexity | Explanation |
| :--- | :--- | :--- |
| **Best Case** | $O(n)$ | The algorithm must always scan every element. |
| **Average Case**| $O(n)$ | The algorithm must always scan every element. |
| **Worst Case** | $O(n)$ | The algorithm must always scan every element. |
| **Space Complexity** | $O(1)$ | It only uses a fixed number of variables. |

-----
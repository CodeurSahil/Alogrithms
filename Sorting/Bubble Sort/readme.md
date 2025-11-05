## 🫧 Bubble Sort

**Bubble Sort** is one of the simplest sorting algorithms, often taught to new programmers because its logic is very easy to understand.

It works by repeatedly stepping through the list, comparing adjacent (side-by-side) elements, and swapping them if they are in the wrong order. This process is repeated until the list is sorted.

The algorithm gets its name from the way larger elements "bubble" up to their correct position at the end of the list, pass by pass.

-----

## ⚙️ The Algorithm (Step-by-Step)

1.  **Start the "Pass":** An outer loop runs from `i = 0` to `len - 1`. Think of `i` as the *number of passes* we've completed. We need `n-1` passes in the worst case.
2.  **Compare and Swap:** An inner loop (`j`) runs from `0` to `len - i - 1`.
      * This loop does the actual work. It compares `arr[j]` with its neighbor `arr[j+1]`.
      * If `arr[j] > arr[j+1]`, it swaps them.
3.  **"Bubble" to the End:** After the first pass (when `i = 0`), the single largest element in the entire array is guaranteed to be at the very end (`arr[len-1]`).
4.  **Shrink the List:** In the next pass (when `i = 1`), the inner loop stops one element earlier (at `len - i - 1`). This is because we *know* the last element is already sorted. This "shrinking" unsorted portion is a key part of the algorithm.
5.  **Repeat:** This continues until the outer loop finishes, by which time all elements have bubbled into their correct sorted positions.

### Visual Example

Let's sort: `[5, 1, 4, 2]`

  * **Pass 1 (i=0):** (Inner loop runs 3 times)

      * Compare `[**5, 1**]`: 5 \> 1. **Swap.** -\> `[1, 5, 4, 2]`
      * Compare `[1, **5, 4**]`: 5 \> 4. **Swap.** -\> `[1, 4, 5, 2]`
      * Compare `[1, 4, **5, 2**]`: 5 \> 2. **Swap.** -\> `[1, 4, 2, 5]`
      * *Pass 1 is done. The largest item (5) is at the end.*

  * **Pass 2 (i=1):** (Inner loop runs 2 times)

      * Compare `[**1, 4**]`: 1 \< 4. No swap. -\> `[1, 4, 2, 5]`
      * Compare `[1, **4, 2**]`: 4 \> 2. **Swap.** -\> `[1, 2, 4, 5]`
      * *Pass 2 is done. The next largest item (4) is in place.*

  * **Pass 3 (i=2):** (Inner loop runs 1 time)

      * Compare `[**1, 2**]`: 1 \< 2. No swap. -\> `[1, 2, 4, 5]`
      * *Pass 3 is done. The next largest item (2) is in place.*

  * **Final Array:** `[1, 2, 4, 5]`

-----

## 🔑 Key Properties

  * **In-place:** Yes. It sorts the array by modifying it directly and only requires one extra temporary variable (`tmp`) for swapping. Its space complexity is **$O(1)$**.
  * **Stable:** Yes. It is a **stable** sort. If you have two equal elements, the `if (arr[j] > arr[j + 1])` condition will be false, so they will *never* be swapped. This means they stay in their original relative order.
  * **Comparison-based:** Yes. It sorts by comparing elements to each other.

-----

## 👍 Advantages

  * **Simple to Understand:** Its biggest advantage. It's one of the easiest sorting algorithms to understand and implement from scratch.
  * **Memory Efficient:** It requires no extra memory (or $O(1)$ constant space), as it sorts the list "in-place."
  * **Stable:** It preserves the original order of equal items, which is a useful property.

-----

## 👎 Disadvantages

  * **Extremely Slow:** This is its main drawback. A time complexity of **$O(n^2)$** for average and worst cases makes it highly inefficient for any reasonably large dataset.
  * **Not Practical:** It is almost never used in real-world applications because other algorithms (like Insertion Sort, Merge Sort, or Quick Sort) are dramatically faster.
  * **Too Many Swaps:** It performs a large number of swaps, which can be computationally expensive.

-----

## 💡 Applications

Because it's so inefficient, Bubble Sort has very few real-world applications:

1.  **Educational Tool:** Its primary use is in computer science courses to teach the fundamentals of sorting, algorithm analysis, and time complexity (like $O(n^2)$).
2.  **Trivial Datasets:** It's acceptable if you *know* you are only sorting an extremely small and fixed number of items (e.g., less than 10-20).

-----

## 📊 Time Complexity Summary

| Case | Complexity | Explanation |
| :--- | :--- | :--- |
| **Best Case** | $O(n)$ | As We are usin Swapped Variable. |
| **Average Case** | $O(n^2)$ | The array is in random order. |
| **Worst Case** | $O(n^2)$ | The array is sorted in **reverse** order (e.g., `[5, 4, 3, 2, 1]`). This forces the maximum number of swaps. |
| **Space Complexity**| $O(1)$ | It's an in-place sort. |

-----
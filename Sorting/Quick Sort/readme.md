## Quick Sort

**Quick Sort** is an efficient, in-place, comparison-based sorting algorithm. Developed by Tony Hoare in 1959, it's one of the most widely used sorting algorithms due to its fast average-case performance.

Its strategy is **"Divide and Conquer,"** similar to Merge Sort. However, Quick Sort's real work happens *before* the recursive calls (in the "divide" step), while Merge Sort's work happens *after* (in the "combine" step).

The core idea is to select an element from the array, called the **pivot**, and partition the other elements into two sub-arrays:

1.  Elements **less than** the pivot.
2.  Elements **greater than** the pivot.

The algorithm then recursively sorts these sub-arrays.

-----

## ⚙️ The Algorithm (Divide and Conquer)

Quick Sort has three main steps:

1.  **Divide (The "Partition" Step):**

      * **Choose a Pivot:** Select one element from the array. This can be the first element, the last element, a random element, or the median. The choice of pivot is *critical* to the algorithm's performance. (We'll use the last element in our code example).
      * **Partition:** Rearrange the array so that all elements smaller than the pivot are to its left, and all elements greater are to its right. The pivot itself ends up in its final, sorted position.
      * This step returns the final index of the pivot.

2.  **Conquer (The "Recursive" Step):**

      * Recursively call Quick Sort on the sub-array to the **left** of the pivot (elements smaller than it).
      * Recursively call Quick Sort on the sub-array to the **right** of the pivot (elements greater than it).

3.  **Combine:**

      * Nothing\! Because the pivot is already in its correct, final place and the sub-arrays are sorted in-place, no "combine" step is needed. The array is sorted once the recursion finishes.

### Partitioning in Detail (Lomuto Partition Scheme)

This is the most common and an intuitive way to partition:

1.  Take the **last element** as the pivot.
2.  Set a "partition index" (let's call it `i`) at the start of the array.
3.  Iterate through the array (with a second index, `j`) from the start up to the element *before* the pivot.
4.  If the element `arr[j]` is **less than or equal to** the pivot, swap `arr[j]` with `arr[i]` and increment `i`.
5.  After the loop, `i` is pointing to the spot where the pivot *should* go. Swap the pivot (at the end) with `arr[i]`.
6.  Return `i`, which is now the pivot's final resting place.

-----

## 🔑 Key Properties

  * **In-place:** Yes. It sorts by modifying the array directly. It only requires a small amount of extra memory ($O(\log n)$) for the recursion call stack.
  * **Stable:** No. It is an **unstable** sort. The relative order of equal elements is *not* guaranteed to be preserved. For example, if you sort `[5a, 3, 5b]`, the result might be `[3, 5b, 5a]`.
  * **Comparison-based:** Yes, it works by comparing elements.
  * **Adaptive:** No, not in its basic form. An already-sorted array can actually trigger its worst-case performance (if the pivot is chosen poorly).

-----

## 👍 Advantages

  * **Fast Average-Case:** $O(n \log n)$ average time is one of the fastest. In practice, it often outperforms Merge Sort and Heap Sort due to a smaller constant factor and good cache locality.
  * **Low Memory Usage:** It's an in-place sort, requiring only $O(\log n)$ average space for the recursion stack (unlike Merge Sort's $O(n)$).
  * **Efficient for Large Datasets:** It's a "general-purpose" sort, working well on most real-world data.

-----

## 👎 Disadvantages

  * **Worst-Case Performance:** Its biggest weakness is a worst-case time complexity of **$O(n^2)$**. This happens when the partitions are extremely unbalanced.
      * **When does this occur?** If the array is **already sorted** (or reverse-sorted) and you consistently pick the first or last element as the pivot. Each partition will be $n-1$ and $0$, leading to $O(n^2)$ behavior.
  * **Not Stable:** As mentioned, it doesn't preserve the relative order of equal items, making it unsuitable for certain tasks.
  * **Slightly Complex:** The partition logic is non-trivial to implement correctly compared to simpler sorts.

-----

## 💡 Applications

  * **Standard Libraries:** Many language `sort()` functions (like C's `qsort`) are based on Quick Sort.
  * **Hybrid Sorts:** It's the core of **Introsort**, which is a hybrid algorithm used by many C++ and .NET sorting libraries. Introsort uses Quick Sort but switches to Heap Sort if the recursion depth gets too large (to avoid the $O(n^2)$ case).
  * **General-Purpose Sorting:** When you need a fast, in-memory sort and stability isn't a requirement, Quick Sort is often the default choice.

-----

## 📊 Time Complexity Summary

| Case | Complexity | Explanation |
| :--- | :--- | :--- |
| **Best Case** | $O(n \log n)$ | The pivot always picks the median. Partitions are perfectly balanced ($n/2$). |
| **Average Case** | $O(n \log n)$ | Partitions are reasonably balanced on average. |
| **Worst Case** | $O(n^2)$ | The pivot always picks the smallest or largest element. Partitions are $n-1$ and $0$. |
| **Space Complexity** | $O(\log n)$ | **Average** (for the recursion call stack). |
| | $O(n)$ | **Worst Case** (for the stack, if partitions are fully unbalanced). |

-----

## ✨ Other Things You Should Know

### 1\. The Pivot is Everything

The $O(n^2)$ worst case is a real problem, but it's almost always avoidable with a smart pivot strategy.

  * **Bad Strategy:** Always picking the first or last element. This fails on sorted/reverse-sorted data.
  * **Good Strategy: Randomized Pivot:** Pick a *random* element from the array as the pivot. This makes the $O(n^2)$ case astronomically unlikely.
  * **Better Strategy: Median-of-Three:** Take the first, middle, and last elements of the array. Find their median, and use *that* as the pivot. This makes it much harder to get a pathologically bad pivot.

### 2\. Quickselect

The partitioning logic of Quick Sort is incredibly useful on its own. If you only want to find the **k-th smallest element** in an array (e.g., the median), you can use the partition method.

You partition the array, get the pivot's index, and then *only* recursively search the side (left or right) where the k-th element must be. This algorithm is called **Quickselect** and has an average-case time of **$O(n)$**, which is much faster than sorting the entire $O(n \log n)$ array.

### 3\. Introsort (Quick Sort's Big Brother)

Because of the $O(n^2)$ risk, most modern libraries don't use *pure* Quick Sort. They use **Introsort**:

1.  **Start** with Quick Sort.
2.  **Track** the recursion depth.
3.  **If** the depth exceeds a certain limit (e.g., $2 \times \log n$), it assumes the worst case is happening and switches to **Heap Sort** (which has a guaranteed $O(n \log n)$ worst case).
4.  **In addition,** for very small sub-arrays (e.g., $n < 16$), it switches to **Insertion Sort**, which is faster for tiny lists due to its low overhead.
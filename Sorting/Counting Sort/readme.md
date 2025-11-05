## 📈 Counting Sort

**Counting Sort** is a highly efficient, non-comparison-based sorting algorithm. It's an **integer sorting** algorithm, meaning it's designed to sort collections of objects that can be mapped to integer keys.

Unlike algorithms like Bubble Sort or Quick Sort, it *does not* compare elements to each other. Instead, it works by creating a "histogram" or "count" of how many times each distinct element appears in the input. It then uses this count information to place the elements into their correct sorted positions.

This "no comparisons" approach allows it to achieve a **linear time complexity $O(n+k)$**, which is faster than the $O(n \log n)$ limit of all comparison-based sorts (like Merge Sort or Quick Sort).

-----

## ⚙️ The Algorithm (Step-by-Step)

The version of the algorithm implemented here is a simple, non-stable version. The full, classic algorithm (which is stable) is slightly different.

Here is the simple version, which this code follows:

1.  **Identify Range:** Know the maximum ($max$) and minimum ($min$) values. In this code, this is hardcoded to $min=0$ and $max=9$. The range $k$ is $max - min + 1$.
2.  **Create Count Array:** Create an auxiliary array (the `countArr`) of size $k$ (10, in this case). Initialize all its values to 0.
3.  **Store Frequencies:** Iterate through the original input `arr` (an $O(n)$ operation). For each `value`, increment its corresponding index in the count array: `countArr[value]++`.
      * (This code does this in the first `for` loop).
4.  **Rebuild the Array:** Iterate through the `countArr` from $min$ to $max$. For each index `j` in the count array:
      * Get the `count` (how many times `j` appeared).
      * Place the value `j` back into the original `arr` `count` times, advancing the insertion index `i` each time.
      * (This is exactly what the second `for` loop does).

-----

## 🔑 Key Properties

  * **Non-Comparison:** It sorts without ever comparing two elements from the input array. This is *why* it can be faster than $O(n \log n)$.
  * **Out-of-Place:** It requires extra memory to store the count array. The space complexity is $O(k)$. (More complex, stable versions require $O(n+k)$).
  * **Integer-Based:** It only works on integers or data that can be mapped to a discrete integer range (like characters, which are just ASCII/UTF-8 integers).
  * **Stability:** This is important. This simple implementation is **NOT STABLE**. A stable sort preserves the original order of equal elements. The classic version *is* stable (more on this below).

-----

## 👍 Advantages

  * **Extremely Fast (Linear Time):** Its $O(n+k)$ complexity is its greatest strength. When the range $k$ is small or proportional to $n$ (i.e., $k = O(n)$), the complexity becomes $O(n)$, which is the fastest possible sorting time.
  * **Simple Logic:** The simple version (like the one here) is very easy to understand and implement.

-----

## 👎 Disadvantages

  * **Range Dependency:** This is its greatest weakness. The algorithm's performance and memory usage are tied directly to the range $k$. If you sort 100 numbers ($n=100$) but their values are between 0 and 1,000,000,000 ($k=10^9$), you would need an array with 1 billion slots. This would be incredibly slow and memory-intensive.
  * **Not In-Place:** It always requires $O(k)$ or $O(n+k)$ extra space, unlike in-place algorithms like Quick Sort (optimized) or Bubble Sort.
  * **Limited Data Types:** It doesn't work on floats, strings, or complex objects directly.

-----

## 💡 Applications

1.  **Radix Sort:** This is its most famous application. Counting Sort is used as the stable "sub-routine" to sort digits in **Radix Sort**.
2.  **Small-Range Data:** Any time you are sorting data with a known, small range.
      * Sorting ages of a population (range 0-120).
      * Sorting test scores (range 0-100).
      * Example: sorting digits (range 0-9).
3.  **Histograms:** The first step of the algorithm is literally creating a frequency histogram, so it's used in data analysis.

-----

## 📊 Time Complexity Summary

| Case | Complexity | Explanation |
| :--- | :--- | :--- |
| **Best Case** | $O(n+k)$ | Must iterate through all $n$ items and all $k$ counts. |
| **Average Case**| $O(n+k)$ | Always the same, regardless of data order. |
| **Worst Case** | $O(n+k)$ | Always the same, regardless of data order. |
| **Space Complexity** | $O(n+k)$ | $O(k)$ for the count array and $O(n)$ for the output array (in the stable version). The simple version is $O(k)$. |

> **Why this code is $O(N)$:**
> The time complexity is $O(N + k)$. In the `main` function, $k$ is constrained to be 10. Since $k$ is a fixed constant, $O(N + 10)$ simplifies to **$O(N)$**. The analysis in the comments was spot on\!

-----

## ✨ Other Things You Should Know

### 1\. The "Stable" Counting Sort

This is the most important concept to add. This implementation is simple but **unstable**. If there are two "5"s in the array, `[5a, 3, 5b]`, the output will be `[3, 5, 5]`, and it's impossible to know which 5 came first.

The **classic, stable** version is more complex and is required for Radix Sort. It works like this:

1.  **Create Count Array:** Same as before (e.g., `[3, 1, 4, 2]` -\> `count[1]=1`, `count[2]=1`, `count[3]=1`, `count[4]=1`).
2.  **Create Cumulative Sum:** Modify the count array so each element stores the *sum of all previous counts*. This tells you the *final position* of the last element of that value.
      * `count[i] = count[i] + count[i-1]`
      * This transforms the count array into a "position" array.
3.  **Create Output Array:** Create a new `output` array of size $n$.
4.  **Build Output (Backwards):** Iterate through the *input* array **backwards** (this is the key to stability).
      * Get the `value` (e.g., `arr[i]`).
      * Find its position from the cumulative `count` array: `pos = count[value] - 1`.
      * Place the element: `output[pos] = value`.
      * Decrement the count for that value: `count[value]--`.
5.  **Copy Back:** Copy the sorted `output` array back to the original `arr`.

<!-- end list -->

```
Example:- 

arr = [3,1,1,4,2]
count = [0,2,1,1,1]  (After step 1, assuming 0-indexed for 0-4 range)

count = [0,2,3,4,5]  (After step 2, cumulative sum)

output = [0,0,0,0,0]

Iterating backwards from arr[4] = 2:
    count[2] = 3
    pos = 3 - 1 = 2
    output[2] = 2
    output = [0,0,2,0,0]
    count[2]--
    count = [0,2,2,4,5]

From arr[3] = 4:
    count[4] = 5
    pos = 5 - 1 = 4
    output[4] = 4
    output = [0,0,2,0,4]
    count[4]--
    count = [0,2,2,4,4]

From arr[2] = 1: (This is the second '1')
    count[1] = 2
    pos = 2 - 1 = 1
    output[1] = 1
    output = [0,1,2,0,4]
    count[1]--
    count = [0,1,2,4,4]    

From arr[1] = 1: (This is the first '1')
    count[1] = 1
    pos = 1 - 1 = 0
    output[0] = 1
    output = [1,1,2,0,4]
    count[1]--
    count = [0,0,2,4,4]

From arr[0] = 3:
    count[3] = 4
    pos = 4 - 1 = 3
    output[3] = 3
    output = [1,1,2,3,4]
    count[3]--
    count = [0,0,2,3,4]

Final Output: [1, 1, 2, 3, 4]
```

### 2\. Handling Negative Numbers

This version only works for non-negative numbers (0-9). To sort negative numbers, one must use an **offset**.

1.  Find the `min` value in the array (e.g., `-5`).
2.  The `countArr` index will now be `value - min`.
3.  When rebuilding, the value to place back is `j + min`.
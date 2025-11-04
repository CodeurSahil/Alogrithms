## Insertion Sort

Insertion Sort is a simple, intuitive, and comparison-based sorting algorithm. The strategy it uses is very similar to how many people sort a hand of playing cards.

The algorithm works by building a final sorted array (or list) one element at a time. It assumes the first element is already sorted. Then, it takes the second element and "inserts" it into the correct position relative to the first. It continues this process, taking the next unsorted element and inserting it into its correct place within the **already-sorted** portion of the array.

-----

## ⚙️ The Algorithm (Step-by-Step)

Insertion Sort splits the array into two conceptual parts: a **sorted sublist** at the beginning and an **unsorted sublist** at the end.

1.  **Start:** The first element (at index 0) is considered the initial sorted sublist.
2.  **Iterate:** Begin with the second element (at index 1). This is the first element to be "inserted."
3.  **Store the Key:** Store the value of this element in a temporary variable (let's call it `key`).
4.  **Shift:** Compare the `key` with the elements in the sorted sublist, moving from right to left (starting from the element just before the `key`).
5.  **Make Space:** If an element in the sorted sublist is **greater** than the `key`, shift that element one position to the right to make space.
6.  **Repeat Shift:** Continue shifting elements to the right as long as they are greater than the `key` or until you reach the beginning of the array.
7.  **Insert:** Once you find a position where the element to the left is smaller than or equal to the `key` (or you've reached the start), insert the `key` into that "empty" slot.
8.  **Continue:** Repeat steps 2-7 for the next element in the unsorted portion, growing the sorted sublist by one each time.
9.  **Finish:** The algorithm is complete when all elements have been inserted into the sorted sublist.

### Visual Example

Let's sort the array: `[5, 2, 4, 6, 1, 3]`

> **Sorted sublist is in `** **`.**

  * **Initial State:** `[5, 2, 4, 6, 1, 3]`

      * Sorted sublist: `[5]`

  * **Iteration 1 (Key = 2):**

      * Compare 2 with 5.
      * 5 \> 2, so shift 5 to the right: `[5, 2, 4, 6, 1, 3]`
      * Insert 2 at the beginning: `[**2, 5**, 4, 6, 1, 3]`

  * **Iteration 2 (Key = 4):**

      * Compare 4 with 5.
      * 5 \> 4, so shift 5 to the right: `[2, 5, 4, 6, 1, 3]`
      * Compare 4 with 2.
      * 2 \< 4, so stop. Insert 4 after 2: `[**2, 4, 5**, 6, 1, 3]`

  * **Iteration 3 (Key = 6):**

      * Compare 6 with 5.
      * 5 \< 6, so stop. Insert 6 after 5: `[**2, 4, 5, 6**, 1, 3]` (No shifts needed)

  * **Iteration 4 (Key = 1):**

      * Compare 1 with 6. 6 \> 1, shift: `[2, 4, 5, 6, 1, 3]`
      * Compare 1 with 5. 5 \> 1, shift: `[2, 4, 5, 1, 6, 3]`
      * Compare 1 with 4. 4 \> 1, shift: `[2, 4, 1, 5, 6, 3]`
      * Compare 1 with 2. 2 \> 1, shift: `[2, 1, 4, 5, 6, 3]`
      * Insert 1 at the beginning: `[**1, 2, 4, 5, 6**, 3]`

  * **Iteration 5 (Key = 3):**

      * Compare 3 with 6. 6 \> 3, shift: `[1, 2, 4, 5, 6, 3]`
      * Compare 3 with 5. 5 \> 3, shift: `[1, 2, 4, 5, 3, 6]`
      * Compare 3 with 4. 4 \> 3, shift: `[1, 2, 4, 3, 5, 6]`
      * Compare 3 with 2.
      * 2 \< 3, so stop. Insert 3 after 2: `[**1, 2, 3, 4, 5, 6**]`

  * **Final Array:** `[1, 2, 3, 4, 5, 6]`

-----

## 🔑 Key Properties

  * **In-place:** It sorts the array without requiring significant extra memory. The space complexity is **O(1)**.
  * **Stable:** It does **not** change the relative order of elements with equal values. If two "5s" are in the array, their original order will be preserved.
  * **Adaptive:** It is very fast if the array is already "mostly sorted." If the array is fully sorted, it runs in **O(n)** time.
  * **Online:** It can sort a list as it receives it, meaning it doesn't need the entire dataset to be available at the start.

-----

## 👍 Advantages

  * **Simple to Implement:** The logic is straightforward and easy to code.
  * **Efficient for Small Datasets:** For small `n`, it is often faster than more complex O(n log n) algorithms like Quicksort or Mergesort (due to lower overhead).
  * **Excellent for Nearly-Sorted Data:** This is its biggest strength. If your data is almost in order, Insertion Sort runs very quickly (close to O(n)).
  * **Stable:** Preserves the relative order of equal keys, which is important for some applications.
  * **In-place:** Requires only a constant amount of extra memory (O(1)).
  * **Online:** It can sort elements as they arrive.

-----

## 👎 Disadvantages

  * **Inefficient for Large Datasets:** Its average and worst-case time complexity of **O(n²)** makes it very slow for large, unsorted lists.
  * **Many Comparisons and Shifts:** For a reverse-sorted list (the worst case), it has to perform the maximum number of comparisons and shifts for every single element.

-----

## 💡 Applications

You'll find Insertion Sort used in the following scenarios:

1.  **Small Datasets:** When you know the list will only ever have a few elements (e.g., less than 15-20).
2.  **Nearly-Sorted Data:** When you are receiving data that is already mostly in order and just needs a few "touch-ups."
3.  **Hybrid Sorting:** This is its most common modern use. More advanced algorithms like **Timsort** (used in Python and Java) and **Introsort** (used in some C++ `std::sort` implementations) switch to Insertion Sort to sort small partitions of the array, as it's faster for those small chunks.
4.  **Online Sorting:** When data arrives in a stream and needs to be kept sorted at all times.

-----

## 📊 Time Complexity Summary

| Case | Complexity | Explanation |
| :--- | :--- | :--- |
| **Best Case** | $O(n)$ | The array is already sorted. The inner loop never runs. |
| **Average Case** | $O(n^2)$ | The array is in random order. |
| **Worst Case** | $O(n^2)$ | The array is sorted in **reverse** order. |
| **Space Complexity** | $O(1)$ | It's an in-place sort. |
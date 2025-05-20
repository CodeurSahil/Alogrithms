# 📘 Quick Sort - Complete Guide

---

## 📌 Introduction

**Quick Sort** is a **divide-and-conquer** sorting algorithm that works by selecting a **pivot** element and partitioning the array into two sub-arrays:
- Elements less than the pivot
- Elements greater than the pivot

These sub-arrays are then recursively sorted.

---

## ⚙️ How It Works

1. **Choose a Pivot** (e.g., last element, first, or random).
2. **Partition** the array:
   - Rearrange elements so that all values less than pivot are to the left, and greater are to the right.
3. **Recursively** apply Quick Sort to left and right sub-arrays.

---

## 🔁 Quick Sort Algorithm (Steps)

1. Pick a pivot element.
2. Partition the array:
   - Place pivot at its correct position.
   - Move smaller elements to left, larger to right.
3. Apply Quick Sort to the left and right of the pivot.

---

## 🔎 Example

Original array:  
`[9, 4, 7, 6, 3, 1, 5]`  
Pivot: `5`  
After partition: `[4, 3, 1] [5] [9, 7, 6]`  
Recursively sort left and right sub-arrays.

---

## ⏱️ Time & Space Complexity

| Case       | Time Complexity |
|------------|-----------------|
| Best Case  | O(n log n)      |
| Average    | O(n log n)      |
| Worst Case | O(n²)           |

- **Space Complexity**: O(log n) for recursion stack

---

## ✅ Advantages

- Faster in practice than many other algorithms like Bubble or Insertion Sort.
- In-place sorting (no extra memory).
- Efficient for large datasets.

---

## ❌ Disadvantages

- Not stable (order of equal elements may change).
- Worst-case time complexity is O(n²).
- Performance depends heavily on pivot selection.

---

## 🧠 Applications

- Used in libraries (like C’s stdlib `qsort()`).
- Efficient for large lists in memory.
- Used in databases and file systems for sorting.

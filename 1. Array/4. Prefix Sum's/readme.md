## 📈 Prefix Sum

A **Prefix Sum** (also known as a cumulative sum, inclusive scan, or running sum) is an array that helps you answer **range sum queries** in constant time.

The core idea is to create a new array, let's call it `prefix`, where each element `prefix[i]` stores the sum of *all* elements in the original array (let's call it `arr`) from the beginning (index 0) up to index `i`.

Think of it like a bank account ledger. If `arr` is your list of daily transactions `[+10, -5, +20, +7]`, the `prefix` array is your account balance on each day `[10, 5, 25, 32]`. If you want to know your net transactions from day 1 to day 3, you can just take your final balance (32) and subtract your starting balance (10) to get 22. Prefix Sum applies this same logic to arrays.

-----

## ⚙️ The Algorithm (Building and Querying)

The technique has two parts: the one-time setup (building the array) and its repeated use (querying). We'll use a **"padded" prefix sum array** (with a leading 0), as it's the cleanest method that avoids all "off-by-one" errors in querying.

**Array (`arr`):** `[10, 2, 8, 5, 3]` (size N=5)

### 1\. Building the Prefix Sum Array

We will create a `prefix` array of size `N + 1` and set `prefix[0] = 0`.

  * `prefix[i]` will store the sum of the first `i` elements of `arr`.
  * `prefix[0] = 0` (The sum of the first 0 elements is 0)
  * `prefix[1] = prefix[0] + arr[0]` = `0 + 10 = 10`
  * `prefix[2] = prefix[1] + arr[1]` = `10 + 2 = 12`
  * `prefix[3] = prefix[2] + arr[2]` = `12 + 8 = 20`
  * `prefix[4] = prefix[3] + arr[3]` = `20 + 5 = 25`
  * `prefix[5] = prefix[4] + arr[4]` = `25 + 3 = 28`

**Final Arrays:**

  * `arr` (0-indexed): `[10, 2, 8, 5, 3]`
  * `prefix` (1-indexed query): `[0, 10, 12, 20, 25, 28]`

### 2\. Querying a Range Sum

Now the magic. To find the sum of `arr` from index `left` to `right` (inclusive):

**`Sum(left, right) = prefix[right + 1] - prefix[left]`**

This formula works for all cases, including `left = 0`.

**Example:** Find the sum of the subarray from index 1 to 3 (`[2, 8, 5]`).

  * `left = 1`, `right = 3`
  * `Sum(1, 3) = prefix[3 + 1] - prefix[1]`
  * `Sum(1, 3) = prefix[4] - prefix[1]`
  * `Sum(1, 3) = 25 - 10 = 15`
  * Check: `2 + 8 + 5 = 15`. It works\!

**Example 2 (with edge case):** Find the sum from index 0 to 2 (`[10, 2, 8]`).

  * `left = 0`, `right = 2`
  * `Sum(0, 2) = prefix[2 + 1] - prefix[0]`
  * `Sum(0, 2) = prefix[3] - prefix[0]`
  * `Sum(0, 2) = 20 - 0 = 20`
  * Check: `10 + 2 + 8 = 20`. It works\!


-----

## 🎯 Where to Use

Use the Prefix Sum technique when:

  * You have a **static (immutable)** array.
  * You need to perform **many range sum queries**.
  * It's a "pre-computation" technique. You do work ($O(N)$) upfront to make future queries ($O(1)$) super fast. If you only have one query, it's faster to just sum the range.

-----

## 🔑 Key Properties

  * **Time-Memory Trade-off:** You use $O(N)$ extra memory to save a lot of query time.
  * **Pre-processing:** The array must be built before it can be queried.
  * **Immutable Data:** It's designed for arrays that *do not change*. If the array changes, the prefix sum array is no longer valid.

-----

## 👍 Advantages

  * **Blazing Fast Queries:** $O(1)$ time for any range sum query. A naive loop would be $O(N)$ for *each* query.
  * **Simple Logic:** The algorithm is very easy to implement and understand.

-----

## 👎 Disadvantages

  * **Inefficient Updates:** This is its main weakness. If you change a single value in `arr[i]`, you must rebuild the *entire* prefix sum array from that point on. This update operation takes $O(N)$ time.
  * **Extra Memory:** It requires $O(N)$ additional space, which could be an issue for extremely large arrays.

> For problems that require *both* frequent range queries and frequent updates, you need a more advanced data structure like a **Binary Indexed Tree (Fenwick Tree)** or a **Segment Tree**.

-----

## 💡 Applications

  * **Equilibrium Index / Pivot Index:** Find an index `i` where the sum of elements to its left equals the sum of elements to its right. With a prefix sum array, you can check any index `i` in $O(1)$ time.
  * **Subarray Sum Problems:** Many "subarray sum" problems can be solved in $O(N)$ time using a prefix sum array combined with a **Hash Map**.
  * **2D Prefix Sums:** This technique can be extended to 2D matrices to find the sum of any submatrix in $O(1)$ time after an $O(N \times M)$ setup.

-----

## 📊 Time Complexity Summary

| Operation | Complexity | Explanation |
| :--- | :--- | :--- |
| **Pre-computation (Build)** | $O(N)$ | You must loop through the array once. |
| **Range Sum Query** | $O(1)$ | It's just one subtraction. |
| **Single Element Update** | $O(N)$ | You must rebuild the prefix array from the updated index. |
| **Space Complexity** | $O(N)$ | To store the `prefix` array. |

-----

## ✨ Other Things You Should Know

### 1\. The "Subarray Sum Equals K" Problem

This is a classic problem that perfectly shows the power of prefix sums.

  * **Problem:** Find the number of contiguous subarrays whose elements sum to `K`.
  * **Solution:**
    1.  Build the prefix sum array `P`.
    2.  We are looking for any two indices, `i` and `j` (with `i > j`), where the sum `arr[j...i]` is `K`.
    3.  This means `P[i] - P[j] = K`.
    4.  Rearranging, we get **`P[j] = P[i] - K`**.
    5.  Iterate through the `prefix` array. At each element `P[i]`, we just need to know how many times we have *already seen* a prefix sum of `P[i] - K`.
    6.  A **Hash Map** is perfect for this. It can store the `{sum: frequency}` of all prefix sums we've encountered so far.
    7.  This combination allows you to solve the problem in a single $O(N)$ pass.

### 2\. 2D Prefix Sum (Submatrix Sum)

You can find the sum of *any* rectangular submatrix in $O(1)$ time.

1.  **Build ( $O(N \times M)$ ):** Create a 2D prefix sum matrix `dp`. `dp[i][j]` is the sum of the rectangle from `(0,0)` to `(i,j)`.
      * `dp[i][j] = arr[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]`
      * (You subtract `dp[i-1][j-1]` because it was double-counted).
2.  **Query ( $O(1)$ ):** To find the sum of a submatrix from `(r1, c1)` to `(r2, c2)`:
      * `Sum = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]`
      * (This is the "inclusion-exclusion principle." You add the `dp[r1-1][c1-1]` back because it was double-subtracted).
## Z-Algorithm

The Z-Algorithm is a powerful and efficient string-processing algorithm that operates in linear time. Its primary function is to find all occurrences of a pattern within a text.

It achieves this by constructing a "Z-array" (or "Z-list") from a given string.

---

## 1. The Z-Array: The Core Concept

The Z-Algorithm is built entirely around the **Z-array**.

For a string `S` of length `n`, the Z-array `Z` is also of length `n`. Each element `Z[i]` stores the length of the **longest substring starting at index `i` that is also a prefix** of the string `S`.

By convention, `Z[0]` is set to 0 (or the string's length), as it's not useful for the algorithm's main operation.

### Example

Let's compute the Z-array for the string `S = "aabaabcaxaabaaba"`.

| Index `i` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| String `S` | a | a | b | a | a | b | c | a | x | a | a | b | a | a | b | a |
| Z-Array `Z` | **0** | **1** | **0** | **2** | **1** | **0** | **0** | **2** | **0** | **6** | **1** | **0** | **3** | **1** | **0** | **1** |

**How to read this:**
* `Z[1] = 1`: The substring at `i=1` is `"aabaabc..."`. The longest prefix that matches is `"a"`. Length is 1.
* `Z[3] = 2`: The substring at `i=3` is `"aabcaxa..."`. The longest prefix that matches is `"aa"`. Length is 2.
* `Z[9] = 6`: The substring at `i=9` is `"aabaaba"`. The longest prefix that matches is `"aabaab"`. Length is 6.

---

## 2. The Algorithm: Building the Z-Array in Linear Time

A naive calculation of the Z-array would take $O(n^2)$ time (for each `i`, compare characters from the start). The brilliance of the Z-Algorithm is that it does this in **$O(n)$** by cleverly reusing past results.

It does this by maintaining a "Z-box" `[L, R]`, which represents the rightmost substring found so far that is also a prefix (i.e., `S[L...R]` matches `S[0...R-L]`).

We iterate through the string with index `i` from 1 to `n-1`:

1.  **Case 1: `i` is outside the Z-box (`i > R`)**
    * We have no information. We perform a simple character-by-character comparison starting at `i`.
    * We set `L = i` and `R = i`.
    * We expand `R` as long as `S[R-L] == S[R]` and `R < n`.
    * We set `Z[i] = R - L` and adjust `R` back by one (`R = R - 1`).

2.  **Case 2: `i` is inside the Z-box (`i <= R`)**
    * This is the clever part. We can use a previously computed value.
    * Let `k = i - L`. This `k` is the "mirrored" position of `i` back in the prefix.
    * We already know `Z[k]`.
    * **Case 2a:** If `Z[k]` is small and fits *inside* the Z-box (i.e., `Z[k] < R - i + 1`), then we know `Z[i] = Z[k]`. We don't need to check.
    * **Case 2b:** If `Z[k]` is large and extends to or *beyond* the Z-box (i.e., `Z[k] >= R - i + 1`), it means `S[i...]` matches *at least* up to `R`. We must then perform a manual comparison starting from `R+1` to see if we can expand the Z-box further. We set `L = i` and continue expanding `R`.



This "Z-box" ensures that each character in the string is visited at most twice, guaranteeing $O(n)$ time complexity.

---

## 3. Where to Use: The Pattern Matching Strategy

The Z-array is the tool; here is how you *use* it for pattern matching.

To find a `Pattern` (length $m$) in a `Text` (length $n$):

1.  **Concatenate:** Create a new string `S = Pattern + "$" + Text`, where `$` is a special character not present in either string.
2.  **Build Z-Array:** Compute the Z-array for this new combined string `S` (length $n+m+1$).
3.  **Scan:** Iterate through the Z-array.
4.  **Find Match:** Any index `i` where `Z[i] == m` signifies a match. This is because the substring starting at `i` matches the prefix of `S` (which is the `Pattern`) for its full length.

### Example:

* `Pattern = "aab"`
* `Text = "baabaa"`
* `S = "aab$baabaa"`

| Index `i` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| String `S` | a | a | b | $ | b | a | a | b | a | a |
| Z-Array `Z` | 0 | 1 | 0 | 0 | 0 | 1 | **3** | 0 | 1 | 1 |

We scan the Z-array and find `Z[6] = 3`. The length of our pattern is 3. This is a match!
The index in the original `Text` is `i - length(Pattern) - 1` = `6 - 3 - 1` = `2`.
`Text[2]` is indeed "aab...".

---

## 4. Advantages 👍 and Disadvantages 👎

### Advantages 👍
* **Linear Time:** Its $O(n+m)$ time complexity is asymptotically optimal.
* **Relative Simplicity:** Many programmers find the core concept of the Z-box easier to understand and implement than the "failure function" (LPS array) used in the KMP algorithm.
* **Versatile:** The Z-array itself has many applications beyond simple pattern matching.

### Disadvantages 👎
* **Space:** It requires $O(n+m)$ extra space for the concatenated string and the Z-array.
* **Not a "Streaming" Algorithm:** Unlike KMP, you cannot easily run the Z-algorithm on a text as it streams in. You must have the entire text and pattern available upfront to create the concatenated string.

---

## 5. Applications

The Z-array is surprisingly versatile:
* **Pattern Matching:** Its main use.
* **Finding All Prefixes:** The Z-array *is* the answer to "find all substrings that are also prefixes."
* **Finding the Period of a String:** Finding the shortest repeating unit in a string.
* **String Compression:** Can be used as a component in compression algorithms.
* **Computational Biology:** Finding repeated sequences in DNA or protein strings.

---

## 6. Z-Algorithm vs. KMP

The Z-Algorithm and the Knuth-Morris-Pratt (KMP) algorithm are the two most famous linear-time string matchers.

| Feature | Z-Algorithm | KMP Algorithm |
| :--- | :--- | :--- |
| **Core Idea** | Builds a **Z-array** on `Pattern + $ + Text`. | Builds a **LPS array** (failure function) on just the `Pattern`. |
| **Matching** | Scans the Z-array for values equal to `len(Pattern)`. | Scans the `Text` once, using the LPS array to "shift" smartly on mismatches. |
| **Time** | $O(n+m)$ | $O(n+m)$ |
| **Space** | $O(n+m)$ | $O(n+m)$ (or $O(m)$ if text isn't stored) |
| **Streaming** | **No.** Requires the full text upfront. | **Yes.** Can process the `Text` as it arrives (online algorithm). |

**Key Takeaway:** If you need to find a pattern in a text that is streaming in (e.g., from a network or large file), **KMP** is the right choice. If you have both strings fully in memory, **Z-Algorithm** is often simpler to code and just as fast.

---

## 7. Time Complexity Summary

* **Preprocessing (Building Z-array):** $O(n+m)$
* **Matching (Scanning Z-array):** $O(n+m)$
* **Total Time Complexity:** $O(n+m)$
* **Space Complexity:** $O(n+m)$
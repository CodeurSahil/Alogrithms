## 📈 Fast and Slow Pointer / Floyd's Tortoise and Hare

The **Fast and Slow Pointer** technique is a specific and powerful pattern of the "Two Pointer" algorithm. It's famously known as **Floyd's Tortoise and Hare** algorithm, named after Robert W. Floyd.

The core idea is to have two pointers, a `slow` pointer and a `fast` pointer, that iterate through a data structure (almost always a **linked list**) at different speeds.
* The **`slow` pointer** (the tortoise) moves one step at a time.
* The **`fast` pointer** (the hare) moves two steps at a time.

By observing how and *if* these pointers meet, you can deduce critical properties of the list, such as whether it has a cycle or where its midpoint is.

---

## ⚙️ The Algorithm (The Mechanism)

The "algorithm" is the *process* of moving the pointers. The specific problem you're solving (like cycle detection or finding the middle) will determine the loop's stopping condition.

### General Movement
1.  **Initialize:**
    * `slow = head`
    * `fast = head`
2.  **Iterate:**
    * Start a loop that continues as long as the `fast` pointer can safely advance. The crucial check is: `while (fast != null && fast.next != null)`
    * Inside the loop, move the pointers:
        * `slow = slow.next` (moves 1 step)
        * `fast = fast.next.next` (moves 2 steps)
3.  **Check Condition:**
    * Inside the loop, you check for your specific goal.
    * *For cycle detection:* `if (slow == fast)` -> A cycle is found.
    * *For finding the middle:* The loop's *termination* gives you the answer. When the loop ends, `slow` will be at the middle.

---

## 🎯 Where to Use

This technique is highly specialized. You should use it almost exclusively when dealing with **Linked List** problems.

* Use it when you need to detect a **cycle** in a linked list.
* Use it when you need to find the **middle** node of a linked list in one pass.
* Use it when you need to find the **start of a cycle**.

---

## 🔑 Key Properties

* **Relative Speed:** The entire technique relies on the *relative speed* between the two pointers (one is twice as fast).
* **In-Place:** It is an in-place algorithm. It doesn't use any extra data structures (like a HashSet, which is the alternative for cycle detection).
* **Guaranteed Meeting:** In a finite cycle, a pointer moving at 2x speed and one at 1x speed are *guaranteed* to meet eventually.

---

## 👍 Advantages

* **🥇 Extreme Space Efficiency:** This is its main advantage. It uses **$O(1)$ space**. The brute-force alternative (using a `HashSet` to store visited nodes) uses $O(N)$ space.
* **Time Efficiency:** It is very fast, solving problems in **$O(N)$** linear time.
* **Elegant:** The code is typically very short and concise.

---

## 👎 Disadvantages

* **Niche Application:** It is not a general-purpose technique. It is almost exclusively for linked lists.
* **Not Intuitive:** While the *code* is simple, the *reason why* it works (especially for finding the cycle's start) is complex and not obvious.
* **Error-Prone:** The `while` loop condition (`fast && fast.next`) is critical and easy to get wrong, leading to `null` pointer exceptions.

---

## 💡 Applications

This technique is used to solve a few classic problems:

### 1. Linked List Cycle Detection (The Hare & Tortoise)
* **Problem:** Does a given linked list have a cycle?
* **Algorithm:**
    1.  Use the standard 1x/2x movement.
    2.  If the loop finishes ( `fast` reaches `null`), there is **no cycle**.
    3.  If `slow == fast` at any point *inside* the loop, there **is a cycle**.

### 2. Find the Middle of a Linked List
* **Problem:** Find the middle node in a single pass.
* **Algorithm:**
    1.  Use the standard 1x/2x movement.
    2.  When the loop terminates (because `fast` or `fast.next` is `null`), the `slow` pointer will be at the middle.
    * If the list has an *even* number of nodes, `slow` will be at the *first* of the two middle nodes (or the *second*, depending on your exact setup).

### 3. Find the Start of a Linked List Cycle
* **Problem:** If there is a cycle, find the *exact node* where the cycle begins.
* **Algorithm (This is a 2-step process):**
    * **Step 1:** Detect the cycle. Run the 1x/2x pointers until they meet at some `meetingPoint`.
    * **Step 2:** Reset one pointer (e.g., `slow`) back to `head`. The other pointer (`fast`) stays at the `meetingPoint`.
    * **Step 3:** Now, move *both* pointers **one step at a time**.
    * The node where they meet *this time* is the **start of the cycle**.

---

## 📊 Time Complexity Summary

| Component | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time** | **$O(N)$** | In a list of $N$ nodes, the `fast` pointer will reach the end in $N/2$ steps. In a list with a cycle, the pointers will meet within a linear number of steps. |
| **Space** | **$O(1)$** | This is the key benefit. No extra data structures are used, only two pointers. |

---

## ✨ Other Things You Should Know

### 1. Why "Find the Start of the Cycle" Works
The math behind the "find the start" algorithm is what makes it so clever.

* Let `k` = distance from `head` to the `cycleStart`.
* Let `m` = distance from `cycleStart` to the `meetingPoint`.
* Let `C` = length of the cycle.

When the pointers meet in Step 1:
* `Distance(slow) = k + m`
* `Distance(fast) = 2 * (k + m)`

Also, `fast`'s distance is `k + m` plus some number of full cycles (`n * C`):
* `Distance(fast) = k + m + n*C`

So: `2 * (k + m) = k + m + n*C`
`k + m = n*C`
`k = n*C - m`

This equation `k = n*C - m` is the magic. It says:
"The distance from the `head` to the `cycleStart` (`k`)" is equal to "The distance from the `meetingPoint` to the `cycleStart` (`C - m`) plus some full cycles (`(n-1)*C`)".

This means if you start one pointer at `head` (distance `k` to go) and one at `meetingPoint` (distance `k` to go), and move them at the *same speed*, they are guaranteed to meet at the `cycleStart`.

### 2. Variation: Nth Node from the End
This is a related two-pointer problem but uses a different "speed" pattern.
1.  **Setup:** `p1` and `p2` both at `head`.
2.  **Head Start:** Move `p1` (the "fast" one) $n$ steps forward.
3.  **Move Together:** Now, move *both* `p1` and `p2` one step at a time, until `p1` reaches the end of the list.
4.  **Result:** When `p1` is at the end, `p2` will be at the $n$-th node from the end.
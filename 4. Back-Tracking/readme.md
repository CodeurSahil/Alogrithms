# 📈 Backtracking

**Backtracking** is a powerful algorithmic *technique* (not a single algorithm) for solving problems by trying to build a solution incrementally, one step at a time. It's a refined form of "brute-force" or depth-first search.

The core idea is to explore a path of choices. If a path leads to a "dead end" (a state that violates the problem's constraints or clearly won't lead to a solution), the algorithm **"backtracks."** This means it undoes its last choice and tries the next available option.

Think of it like navigating a **maze**:

1.  You walk down a path (make a choice).
2.  At a junction, you pick a new path (make another choice).
3.  You continue until you either find the exit (a solution) or hit a wall (a dead end).
4.  When you hit a wall, you don't give up. You go **back** to the last junction you were at and try a *different* path.

-----

## ⚙️ The Algorithm (The General Template)

Backtracking is almost always implemented with **recursion**. It works by maintaining the "current state" of the solution being built.

The process can be simplified to three steps: **Choose, Explore, Unchoose.**

Here is a pseudo-code template that applies to most backtracking problems:

```
function find_solution(current_state):
    
    # Base Case 1: Found a valid, complete solution
    if current_state is a complete_solution:
        add current_state to our list_of_solutions
        return

    # Base Case 2: The path is invalid (dead end)
    if current_state is not_valid:
        return
        
    # --- Recursive Step ---
    for each 'possible_choice' from the current_state:
        
        # 1. CHOOSE
        # Make the choice
        add 'possible_choice' to the current_state
        
        # 2. EXPLORE
        # Recurse with the new state
        find_solution(new_state)
        
        # 3. UNCHOOSE (The "Backtrack" Step)
        # Undo the choice
        remove 'possible_choice' from the current_state
```

The "Unchoose" step is the most critical part. It's what allows the algorithm to "go back" and explore different branches of the decision tree.

-----

## 🎯 Where to Use

You should think of using backtracking when your problem fits these descriptions:

  * **Constraint Satisfaction Problems (CSPs):** The problem requires you to find a solution that satisfies a set of specific rules or constraints (e.g., Sudoku, N-Queens).
  * **"Find all..." Problems:** You need to find *all possible* solutions, not just one (e.g., all permutations of a string, all combinations that sum to a target).
  * **"Find one..." Path Problems:** You need to find *a* valid path or solution (e.g., a path through a maze, a "word break" solution).
  * **Sequential Choices:** The problem can be broken down into a sequence of "choices," where each choice leads to a new, smaller version of the problem.

-----

## 🔑 Key Properties

  * **Depth-First Search (DFS):** Backtracking is a form of DFS. It explores one path to its maximum depth (a "leaf") before backtracking to explore another.
  * **Implicit Graph:** It operates on an "implicit state-space graph," where each node is a `current_state` and each edge is a `choice`.
  * **Pruning:** The "backtrack" (Base Case 2) is a form of "pruning." We are "pruning" (cutting off) entire branches of the search tree that we know are invalid, which is what makes this "smarter" than pure brute-force.
  * **Recursive:** Its most natural and common implementation is recursive.

-----

## 👍 Advantages

  * **Broadly Applicable:** It's a "Swiss Army knife" that can be adapted to solve a huge range of complex problems that don't have a simple, direct solution.
  * **Finds All Solutions:** It is a *complete* algorithm, meaning it's guaranteed to find all possible solutions (if any exist).
  * **Simple to Implement (Recursively):** The recursive "Choose, Explore, Unchoose" template can be very short and elegant, even for hard problems.
  * **Optimizable:** You can easily add more "pruning" logic to make it faster by ruling out bad paths earlier.

-----

## 👎 Disadvantages

  * **Slow (Worst-Case):** The time complexity is often exponential ($O(b^d)$ or $O(N!)$). It's still a brute-force search at its core, just a much smarter one.
  * **Stack Overflow:** Because it's deeply recursive, a very long solution path (deep tree) can cause a stack overflow error.
  * **Redundant Work:** It can sometimes re-calculate the same state multiple times, unlike Dynamic Programming.

-----

## 💡 Applications

  * 🧩 **Puzzles:**
      * Sudoku Solvers
      * N-Queens Problem (Place N queens on a chessboard so none attack each other)
      * Solving Mazes
  * 🧬 **Combinatorics & Permutations:**
      * Generating all permutations of a set
      * Generating all combinations of a set
      * Generating all subsets of a set
  * 🔡 **String Problems:**
      * Generate Parentheses (Find all valid combinations)
      * Word Break (Can a string be segmented into dictionary words?)

-----

## 📊 Time Complexity Summary

This is the trickiest part, as it's not one algorithm. The complexity depends entirely on the problem.

  * **Time:** The general formula is: **$O(b^d)$**
      * `b` = **branching factor** (the number of choices at each step).
      * `d` = **depth** (the length of the longest solution path).
  * **Examples:**
      * **Permutations of `N` items:** $O(N! \times N)$. There are $N!$ solutions, and it takes $O(N)$ time to build/copy each one.
      * **Subsets of `N` items:** $O(2^N \times N)$. There are $2^N$ subsets.
  * **Space:** The space complexity is driven by the call stack.
      * **$O(d)$** or **$O(N)$**, representing the maximum depth of the recursion.
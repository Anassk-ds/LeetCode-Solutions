
# 1569. Number of Ways to Reorder Array to Get Same BST

**Difficulty:** Hard

**Topics:** Binary Search Tree, Recursion, Combinatorics, Dynamic Programming

## Problem

Given a permutation of integers from `1` to `n`, construct a Binary Search Tree (BST) by inserting the elements in order.

Return the number of different reorderings that construct the same BST as the original array, excluding the original ordering.

Return the answer modulo `10^9 + 7`.

## Examples

### Example 1

**Input**
```python
nums = [2, 1, 3]
```

**Output**
```text
1
```

### Example 2

**Input**
```python
nums = [3, 4, 5, 1, 2]
```

**Output**
```text
5
```

### Example 3

**Input**
```python
nums = [1, 2, 3]
```

**Output**
```text
0
```

## Approach

1. Precompute binomial coefficients using Pascal's triangle.
2. Choose the first element as the root of each subtree.
3. Partition the remaining elements into left and right subtrees.
4. Recursively calculate the valid reorderings for both subtrees.
5. Multiply the left and right counts by the number of ways to interleave their elements.
6. Subtract one to exclude the original ordering.

For left subtree size `L` and right subtree size `R`, the number of interleavings is:

`C(L + R, L)`

## Python Solution

```python
import sys

sys.setrecursionlimit(10000)


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        comb = [[0] * n for _ in range(n)]

        for i in range(n):
            comb[i][0] = 1
            for j in range(1, i + 1):
                if j == i:
                    comb[i][j] = 1
                else:
                    comb[i][j] = (
                        comb[i - 1][j - 1] + comb[i - 1][j]
                    ) % MOD

        def count_ways(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = count_ways(left)
            right_ways = count_ways(right)

            interleavings = comb[len(left) + len(right)][len(left)]

            return (
                interleavings * left_ways * right_ways
            ) % MOD

        return (count_ways(nums) - 1) % MOD
```

## Complexity

- **Time:** `O(n^2)`
- **Space:** `O(n^2)`

## Key Concepts

- Binary Search Trees
- Recursive decomposition
- Binomial coefficients
- Pascal's triangle
- Modular arithmetic

## Pattern

**Divide and Conquer + Combinatorics**

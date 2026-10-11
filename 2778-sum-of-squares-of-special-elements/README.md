
# 2778. Sum of Squares of Special Elements

**Difficulty:** Easy

**Topics:** Array, Math

## Problem Statement

You are given a 1-indexed integer array `nums` of length `n`.

An element `nums[i]` is called special if `i` divides `n`, meaning `n % i == 0`.

Return the sum of the squares of all special elements of `nums`.

## Examples

### Example 1

**Input:**
```text
nums = [1, 2, 3, 4]
```

**Output:**
```text
21
```

**Explanation:**

The special indices are 1, 2, and 4.

Sum = 1² + 2² + 4² = 21.

### Example 2

**Input:**
```text
nums = [2, 7, 1, 19, 18, 3]
```

**Output:**
```text
63
```

**Explanation:**

The special indices are 1, 2, 3, and 6.

Sum = 2² + 7² + 1² + 3² = 63.

## Constraints

- `1 <= nums.length == n <= 50`
- `1 <= nums[i] <= 50`

## Approach

1. Find the length `n` of the array.
2. Traverse the array using 1-based indices.
3. If `n % i == 0`, the element is special.
4. Add the square of that element to the total.
5. Return the total.

## Python 3 Solution

```python
class Solution:
    def sumOfSquares(self, nums):
        n = len(nums)
        total = 0

        for i, num in enumerate(nums, start=1):
            if n % i == 0:
                total += num * num

        return total
```

## Complexity Analysis

- **Time Complexity:** O(n)
- **Auxiliary Space Complexity:** O(1)

## Key Concept

Use the modulo operator (`%`) to check divisibility and accumulate the squares of elements at special indices.

## Pattern

Array Traversal + Divisibility + Basic Math

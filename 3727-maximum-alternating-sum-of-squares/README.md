
# 3727. Maximum Alternating Sum of Squares

**Difficulty:** Medium

**Topics:** Greedy, Sorting, Arrays

## Problem Statement

You are given an integer array `nums`. You may rearrange its elements in any order.

The alternating score of an array `arr` is defined as:

`arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...`

Return the maximum possible alternating score after rearranging the elements.

## Examples

### Example 1

**Input:**
```text
nums = [1, 2, 3]
```

**Output:**
```text
12
```

**Explanation:**

One optimal arrangement is `[2, 1, 3]`.

Score = 2² - 1² + 3² = 4 - 1 + 9 = 12.

### Example 2

**Input:**
```text
nums = [1, -1, 2, -2, 3, -3]
```

**Output:**
```text
16
```

**Explanation:**

An optimal arrangement is `[-3, -1, -2, 1, 3, 2]`.

Score = 9 - 1 + 4 - 1 + 9 - 4 = 16.

## Constraints

- `1 <= nums.length <= 10^5`
- `-4 * 10^4 <= nums[i] <= 4 * 10^4`

## Approach: Greedy + Sorting

1. Square every element. The original signs do not matter because each value is squared.
2. Sort the squares in descending order.
3. Assign the largest `ceil(n / 2)` squares to positive positions.
4. Assign the remaining squares to negative positions.
5. Subtract the sum of the negative-position squares from the sum of the positive-position squares.

This arrangement maximizes the alternating score because the largest values receive positive coefficients and the smallest values receive negative coefficients.

## Python 3 Solution

```python
class Solution:
    def maxAlternatingSum(self, nums):
        squares = sorted((num * num for num in nums), reverse=True)
        half = (len(squares) + 1) // 2

        return sum(squares[:half]) - sum(squares[half:])
```

## Complexity Analysis

- **Time Complexity:** O(n log n)
- **Auxiliary Space Complexity:** O(n)

## Key Concepts

- Squaring integers
- Greedy assignment
- Sorting
- Maximizing an alternating sum

## Pattern

Greedy + Sorting + Array Rearrangement


# 2897. Apply Operations on Array to Maximize Sum of Squares

**Difficulty:** Hard

**Topics:** Greedy, Bit Manipulation, Counting

## Problem Statement

You are given a 0-indexed integer array `nums` and a positive integer `k`.

You can perform the following operation any number of times:

Choose two distinct indices `i` and `j`, and simultaneously update:

- `nums[i] = nums[i] AND nums[j]`
- `nums[j] = nums[i] OR nums[j]`

Here, AND and OR are bitwise operations.

Choose `k` elements from the final array and maximize the sum of their squares.

Return the maximum sum modulo `10^9 + 7`.

## Examples

### Example 1

**Input:**
```text
nums = [2, 6, 5, 8], k = 2
```

**Output:**
```text
261
```

**Explanation:**

The selected values can be 15 and 6.

Sum of squares = 15² + 6² = 261.

### Example 2

**Input:**
```text
nums = [4, 5, 4, 7], k = 3
```

**Output:**
```text
90
```

**Explanation:**

Choose 7, 5, and 4.

Sum of squares = 7² + 5² + 4² = 90.

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Approach: Greedy Bit Counting

1. Count how many numbers contain each set bit.
2. Construct each of the `k` numbers by taking every bit with a positive remaining count.
3. Decrease the count of each bit used.
4. Add the square of each constructed number to the answer.
5. Return the result modulo `10^9 + 7`.

Concentrating available set bits into the same number maximizes its value. Repeating this process for `k` numbers maximizes the sum of squares.

## Python 3 Solution

```python
class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        bit_count = [0] * 31

        for num in nums:
            for bit in range(31):
                if num & (1 << bit):
                    bit_count[bit] += 1

        answer = 0

        for _ in range(k):
            value = 0

            for bit in range(31):
                if bit_count[bit] > 0:
                    value |= 1 << bit
                    bit_count[bit] -= 1

            answer = (answer + value * value) % MOD

        return answer
```

## Complexity Analysis

- **Time Complexity:** O(31n + 31k), effectively O(n + k).
- **Auxiliary Space Complexity:** O(1), using a fixed-size bit-count array.

## Key Concepts

- Bitwise AND and OR
- Counting set bits
- Greedy construction
- Maximizing the sum of squares
- Modular arithmetic

## Pattern

Greedy + Bit Manipulation + Frequency Counting

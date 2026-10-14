# 3723. Maximize Sum of Squares of Digits

**Difficulty:** Medium

**Topics:** Greedy, Math, Strings

## Problem Statement

You are given two positive integers `num` and `sum`.

A positive integer `n` is good if:

- It contains exactly `num` digits.
- The sum of its digits is exactly `sum`.

The score of a good integer is the sum of the squares of its digits.

Return the string representing the good integer with the maximum score. If multiple integers have the maximum score, return the largest integer. If no such integer exists, return an empty string.

## Examples

### Example 1

**Input:**
```text
num = 2, sum = 3
```

**Output:**
```text
"30"
```

**Explanation:**

The good integers are 12, 21, and 30.

Their scores are 5, 5, and 9, respectively. Therefore, the answer is "30".

### Example 2

**Input:**
```text
num = 2, sum = 17
```

**Output:**
```text
"98"
```

**Explanation:**

The good integers are 89 and 98. Both have a score of 145, so the larger integer, "98", is returned.

### Example 3

**Input:**
```text
num = 1, sum = 10
```

**Output:**
```text
""
```

**Explanation:**

A single digit cannot have a digit sum of 10.

## Constraints

- `1 <= num <= 2 * 10^5`
- `1 <= sum <= 2 * 10^6`

## Approach: Greedy

1. If `sum > 9 * num`, return an empty string because the required digit sum is impossible.
2. Use as many `9` digits as possible.
3. If a remainder exists and there is room, append that remainder.
4. Fill the remaining positions with zeros.

Placing larger digits first maximizes the integer when scores tie. Concentrating the digit sum into as few digits as possible maximizes the sum of squared digits.

## Python 3 Solution

```python
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        nines, remainder = divmod(sum, 9)
        result = "9" * nines

        if nines < num and remainder > 0:
            result += str(remainder)

        result += "0" * (num - len(result))
        return result
```

## Complexity Analysis

- **Time Complexity:** O(num)
- **Auxiliary Space Complexity:** O(num)

## Key Concepts

- Greedy digit allocation
- Maximizing squared digits
- Digit sum constraints
- Lexicographically largest result

## Pattern

Greedy + Digit Manipulation + String Construction

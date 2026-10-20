
# 3886. Sum of Sortable Integers

**Difficulty:** Hard

**Topics:** Array, Sorting, Number Theory

## Problem Description

Given an integer array `nums` of length `n`, an integer `k` is sortable if:

- `k` divides `n`.
- Partitioning `nums` into consecutive subarrays of length `k` allows each subarray to be independently cyclically rotated into non-decreasing order.

Return the sum of all sortable integers `k`.

## Examples

### Example 1

**Input**
```python
nums = [3, 1, 2]
```

**Output**
```text
3
```

**Explanation:** Only `k = 3` is sortable, so the answer is `3`.

### Example 2

**Input**
```python
nums = [7, 6, 5]
```

**Output**
```text
0
```

**Explanation:** Neither `k = 1` nor `k = 3` allows the array to become sorted.

### Example 3

**Input**
```python
nums = [5, 8]
```

**Output**
```text
3
```

**Explanation:** Both `k = 1` and `k = 2` are sortable. Their sum is `1 + 2 = 3`.

## Approach

1. Find all divisors of `n` by checking integers up to `sqrt(n)`.
2. For each divisor `k`, divide the array into blocks of length `k`.
3. Count circular descents in each block. A descent occurs when an element is greater than the next element, including the comparison between the last and first elements.
4. A block can be cyclically rotated into non-decreasing order if and only if it has at most one circular descent.
5. If every block passes this test, add `k` to the answer.

## Python Solution

```python
class Solution:
    def sumOfSortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = []

        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1

        answer = 0

        for k in divisors:
            sortable = True

            for start in range(0, n, k):
                end = start + k
                descents = 0

                for j in range(start, end - 1):
                    if nums[j] > nums[j + 1]:
                        descents += 1

                if nums[end - 1] > nums[start]:
                    descents += 1

                if descents > 1:
                    sortable = False
                    break

            if sortable:
                answer += k

        return answer
```

## Complexity Analysis

Let `d(n)` be the number of divisors of `n`.

- **Time Complexity:** `O(sqrt(n) + n * d(n))`
- **Space Complexity:** `O(d(n))`

## Key Concepts

- Divisor enumeration
- Cyclic rotations
- Circular descents
- Non-decreasing order
- Array partitioning

## Pattern

**Number Theory + Array Traversal**

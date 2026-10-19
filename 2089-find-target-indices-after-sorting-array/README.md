
# 2089. Find Target Indices After Sorting Array

**Difficulty:** Easy

**Topics:** Array, Sorting

## Problem Description

Given a 0-indexed integer array `nums` and an integer `target`, return the indices where `nums[i] == target` after sorting `nums` in non-decreasing order.

The returned indices must be sorted in increasing order. If the target does not exist, return an empty list.

## Examples

### Example 1

**Input**
```python
nums = [1, 2, 5, 2, 3]
target = 2
```

**Output**
```python
[1, 2]
```

**Explanation:** After sorting, the array is `[1, 2, 2, 3, 5]`. The target occurs at indices 1 and 2.

### Example 2

**Input**
```python
nums = [1, 2, 5, 2, 3]
target = 3
```

**Output**
```python
[3]
```

### Example 3

**Input**
```python
nums = [1, 2, 5, 2, 3]
target = 5
```

**Output**
```python
[4]
```

## Approach

1. Sort the array in non-decreasing order.
2. Traverse the sorted array using `enumerate()` to obtain each element and its index.
3. Collect every index whose element equals `target`.
4. Return the resulting list.

## Python Solution

```python
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i, value in enumerate(nums) if value == target]
```

## Complexity Analysis

- **Time Complexity:** `O(n log n)` due to sorting.
- **Space Complexity:** `O(n)` in the worst case, accounting for sorting implementation and the returned list.

## Key Concepts

- Array sorting
- Zero-based indexing
- Python `enumerate()`
- List comprehensions

## Pattern

**Sorting + Linear Search**

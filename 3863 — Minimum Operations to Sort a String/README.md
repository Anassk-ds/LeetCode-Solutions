## 3863. Minimum Operations to Sort a String

Difficulty: Medium

Topics: String, Greedy

Problem Description

You are given a string "s" consisting of lowercase English letters.

In one operation, you can select any substring of "s" that is not the entire string and sort it in non-descending alphabetical order.

Return the minimum number of operations required to make "s" sorted in non-descending order. If it is not possible, return "-1".

Examples

Example 1

Input

s = "dog"

Output

1

Explanation: Sort the substring ""og"" to obtain ""dgo"".

Example 2

Input

s = "card"

Output

2

Explanation: Sort ""car"" to obtain ""acrd"", then sort ""rd"" to obtain ""acdr"".

Example 3

Input

s = "gf"

Output

-1

Explanation: The only proper substrings of a two-character string have length one, so the characters cannot be rearranged.

Constraints

- "1 <= s.length <= 10^5"
- "s" consists of lowercase English letters.

Approach

1. Check whether the string is already sorted. If it is, return "0".
2. If the string has length "2" and is not sorted, return "-1".
3. Find the minimum and maximum characters in the string.
4. If the first character is the minimum or the last character is the maximum, the answer is "1".
5. Otherwise, check whether the minimum or maximum character appears in the interior of the string. If so, the answer is "2".
6. If none of these conditions apply, the answer is "3".

Python 3 Solution

from itertools import pairwise

class Solution:
    def minOperations(self, s: str) -> int:
        if all(a <= b for a, b in pairwise(s)):
            return 0
        if len(s) == 2:
            return -1
        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        if any(c in [mn, mx] for c in s[1:-1]):
            return 2
        return 3

Complexity Analysis

Let "n" be the length of the string.

- Time Complexity: "O(n)" — checking sorted order, finding the minimum and maximum characters, and examining the interior characters each take linear time.
- Space Complexity: "O(1)" auxiliary space, excluding iterator overhead.

Key Concepts

- String traversal
- Lexicographical ordering
- Minimum and maximum character identification
- Greedy case analysis

Pattern

Greedy + String

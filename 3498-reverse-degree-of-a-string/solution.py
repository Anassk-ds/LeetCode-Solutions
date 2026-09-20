class Solution:
    def reverseDegree(self, s):
        total = 0

        for i, ch in enumerate(s):
            reverse_position = 26 - (ord(ch) - ord('a'))
            string_position = i + 1

            total += reverse_position * string_position

        return total

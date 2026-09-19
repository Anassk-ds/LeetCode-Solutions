class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # Find first and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Try to create a valid substring starting
        # from the first occurrence of each character
        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                # This character appeared before left,
                # so we cannot create a valid substring here
                if first[x] < left:
                    valid = False
                    break

                right = max(right, last[x])
                i += 1

            if valid:
                intervals.append((left, right))

        # Choose intervals greedily by ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        end = -1

        for left, right in intervals:
            if left > end:
                result.append(s[left:right + 1])
                end = right

        return result
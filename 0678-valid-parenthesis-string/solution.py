class Solution:
    def checkValidString(self, s):
        min_open = 0
        max_open = 0

        for ch in s:
            if ch == '(':
                min_open += 1
                max_open += 1

            elif ch == ')':
                min_open -= 1
                max_open -= 1

            else:  # '*'
                min_open -= 1
                max_open += 1

            # Even the maximum possible balance is negative.
            if max_open < 0:
                return False

            # We cannot have a negative minimum balance.
            min_open = max(0, min_open)

        return min_open == 0

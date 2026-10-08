class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = {s}
        result = []

        while queue:
            for string in queue:
                if is_valid(string):
                    result.append(string)

            if result:
                return result

            next_level = set()

            for string in queue:
                for i in range(len(string)):
                    if string[i] not in '()':
                        continue

                    next_level.add(string[:i] + string[i + 1:])

            queue = next_level

        return result
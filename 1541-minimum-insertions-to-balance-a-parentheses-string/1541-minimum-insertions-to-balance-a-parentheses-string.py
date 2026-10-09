class Solution:
    def minInsertions(self, s):
        insertions = 0
        open_count = 0

        i = 0
        while i < len(s):
            if s[i] == '(':
                open_count += 1
            else:
                # Check whether we have two consecutive ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    # Insert a ')' to complete the pair
                    insertions += 1

                if open_count > 0:
                    open_count -= 1
                else:
                    # Insert '(' to match this closing pair
                    insertions += 1

            i += 1

        # Each remaining '(' needs two closing parentheses
        insertions += open_count * 2

        return insertions
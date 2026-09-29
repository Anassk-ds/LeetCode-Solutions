class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length.
        if (m + n - 1) % 2 != 0:
            return False

        # dp[j] contains the possible balance values
        # at column j for the current row.
        dp = [[set() for _ in range(n)] for _ in range(m)]

        if grid[0][0] == ')':
            return False

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                if grid[i][j] == '(':
                    change = 1
                else:
                    change = -1

                possible_balances = set()

                if i > 0:
                    possible_balances.update(dp[i - 1][j])

                if j > 0:
                    possible_balances.update(dp[i][j - 1])

                for balance in possible_balances:
                    new_balance = balance + change

                    # A valid parentheses string can never
                    # have a negative balance.
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]
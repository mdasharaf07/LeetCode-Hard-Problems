class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []

        def solve(row, queens, cols, diag1, diag2):
            if row == n:
                board = ["".join('Q' if c == queens[i] else '.' for c in range(n)) for i in range(n)]
                res.append(board)
                return
            for col in range(n):
                if cols[col] or diag1[row + col] or diag2[row - col + n - 1]:
                    continue
                queens[row] = col
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
                solve(row + 1, queens, cols, diag1, diag2)
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

        solve(0, [0]*n, [False]*n, [False]*(2*n-1), [False]*(2*n-1))
        return res
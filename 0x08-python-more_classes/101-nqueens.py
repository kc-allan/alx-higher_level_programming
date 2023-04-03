#!/usr/bin/python3
import sys
"""Defines NQieens"""


class NQueens:
    """Represents NQueens"""
    def __init__(self, n):
        """Initializes the class"""
        self.n = n
        self.board = [['.' for x in range(n)] for y in range(n)]
        self.solutions = []

    def solve(self):
        """Prints valid squares for all posibble combinations"""
        self._solve_helper(0)
        for solution in self.solutions:
            print(self._valid_squares(solution))

    def _solve_helper(self, col):
        """Checks valid squares in one combination"""
        if col == self.n:
            self.solutions.append([row[:] for row in self.board])
            return
        for row in range(self.n):
            if self._is_safe(row, col):
                self.board[row][col] = 'Q'
                self._solve_helper(col+1)
                self.board[row][col] = '.'

    def _is_safe(self, row, col):
        """Checks if a square is valid for olacing a queen"""
        for i in range(col):
            if self.board[row][i] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j] == 'Q':
                return False
        return True

    def _valid_squares(self, board):
        """Checks valid square"""
        valid = []
        for i in range(self.n):
            for k in range(self.n):
                if board[i][k] == 'Q':
                    valid.append([i, k])
        return valid


def main():
    """Entry point"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    queens = NQueens(n)
    queens.solve()


if __name__ == '__main__':
    main()

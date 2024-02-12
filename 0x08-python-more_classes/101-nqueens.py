#!/usr/bin/python3
import sys

class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(self, board, col):
        if col >= self.n:
            solution = []
            for i in range(self.n):
                for j in range(self.n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            self.solutions.append(solution)
            return
        for i in range(self.n):
            if self.is_safe(board, i, col):
                board[i][col] = 1
                self.solve(board, col + 1)
                board[i][col] = 0

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    queens = NQueens(n)
    board = [[0 for _ in range(n)] for _ in range(n)]
    queens.solve(board, 0)
    for sol in queens.solutions:
        print(sol)

if __name__ == "__main__":
    main()


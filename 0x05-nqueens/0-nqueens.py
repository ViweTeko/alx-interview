#!/usr/bin/python3
""" N Queens"""
from sys import argv, exit


def solve_nqueens(z):
    """Print board configuration"""
    board = [[0 for _ in range(z)] for _ in range(z)]
    if not solve_nqueens_util(board, 0):
        print('No solution exists')


def solve_nqueens_util(board, column):
    """Solves N-Queens problem by backtracking"""
    if column >= len(board):
        print_solution(board)
        return True
    result = False
    for x in range(len(board)):
        if is_safe(board, x, column):
            board[x][column] = 1
            result = solve_nqueens_util(board, column + 1) or result
            board[x][column] = 0
    return result


def is_safe(board, row, column):
    """Checks safety of placing queen at board[row][col]"""
    for a in range(column):
        if board[row][a] == 1:
            return False

    for x, y in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[x][y] == 1:
            return False

    for x, y in zip(range(row, len(board), 1), range(column, -1, -1)):
        if board[x][y] == 1:
            return False
    return True


def print_solution(board):
    """Prints board configuration"""
    solution = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1:
                solution.append([x, y])
    print(solution)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        b = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if b < 4:
        print("N must be at least 4")
        exit(1)

    solve_nqueens(b)

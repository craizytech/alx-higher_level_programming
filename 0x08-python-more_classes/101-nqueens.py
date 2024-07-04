#!/usr/bin/python3
"""This module here defines the Solutions for nqueens problem"""

import sys


def main():
    """This is the main/driver function of the program."""
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Try converting the number to an integer
        N = int(sys.argv[1])
    except ValueError:
        # If conversion fails, the input is not a number
        print("N must be a number")
        sys.exit(1)

    # Check if N is atleast 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the solutions list and the board
    solutions = []
    board = [[0] * N for _ in range(N)]

    # Call the solve function starting from the first row
    solve(board, 0, N, solutions)

    # Print each solution
    for solution in solutions:
        print(solution)


def solve(board, row, N, solutions):
    """
    Recursive function to solve the N-Queens problem using backtracking

    Args:
        board (matrix): the current state of the chessboard
        row: The current row to place a queen
        N: The size of the chessboard (NxN)
        solutions: List to store all valid solutions
    """
    # If all queens are placed, add the solution to the solution list
    if row == N:
        solutions.append(convert_board_to_solution_format(board, N))
        return

    # Iterate over each column in the current row
    for col in range(N):
        if is_valid(board, row, col, N):
            # Place the queen if it's a valid position
            board[row][col] = 1
            # Recurse to place the next queen in the next row
            solve(board, row + 1, N, solutions)
            # Backtrack: remove the queen and try the next column
            board[row][col] = 0


def is_valid(board, row, col, N):
    """
    checks if its safe to place a queen at board[row][col].

    Args:
        board: the current state of the chessboard
        row: the row to check
        col: the column to check
        N: The size of the chessboard (N x N)
    Returns: True if it is safe to place the queen, False otherwise
    """
    # Check the column for any other queens
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the major diagonal (top-left to bottom-right)
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the minor diagonal (top-right to bottom-left)
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j] == 1:
            return False

    return True


def convert_board_to_solution_format(board, N):
    """
    Convert the board to the required solution format.

    Args:
        board: The current state of the chessboard
        N: The size of the chessboard (N x N)
    Returns:
        A list of [row, col] pairs where queens are placed
    """
    solution = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                solution.append([row, col])
    return solution


if __name__ == "__main__":
    main()

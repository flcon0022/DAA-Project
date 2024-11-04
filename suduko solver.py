def print_board(board):
    """function to print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) for num in row))

def find_empty(board):
    """Find an empty space in the Sudoku board (represented by 0)."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Row, Column
    return None

def is_valid(board, num, row, col):
    """Check if placing num at board[row][col] is valid."""
    # Check the row
    if num in board[row]:
        return False

    # Check the column
    for r in range(9):
        if board[r][col] == num:
            return False

    # Check the 3x3 grid
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == num:
                return False

    return True

def solve_sudoku(board):
    
    #Solve the Sudoku puzzle using backtracking.

    empty = find_empty(board)
    if not empty:
        return True  # No empty space left, puzzle solved

    row, col = empty

    for num in range(1, 10):  # Numbers 1-9
        if is_valid(board, num, row, col):
            board[row][col] = num  # Place the number

            if solve_sudoku(board):
                return True  # If successful, return

            board[row][col] = 0  # Backtrack

    return False  # Trigger backtracking

# Example Sudoku board (0s represent empty spaces)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

if __name__ == "__main__":
    print("Original Sudoku Board:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Board:")
        print_board(sudoku_board)
    else:
        print("No solution exists.")



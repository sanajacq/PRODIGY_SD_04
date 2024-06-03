def is_valid(board, row, col, num):
    
    if num in board[row]:
        return False

    
    for i in range(9):
        if board[i][col] == num:
            return False

    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_location(board)

    
    if row is None:
        return True

    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            
            if solve_sudoku(board):
                return True

            
            board[row][col] = 0

    
    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def main():
    print("Enter the Sudoku puzzle (9x9 grid, use 0 for empty cells):")
    puzzle = []
    for _ in range(9):
        row = list(map(int, input().split()))
        puzzle.append(row)

    if solve_sudoku(puzzle):
        print("\nSudoku puzzle solved:")
        print_board(puzzle)
    else:
        print("\nNo solution exists for the given puzzle.")

if __name__ == "__main__":
    main()

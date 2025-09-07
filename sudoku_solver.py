# Code Author: Avery Leber
# 09-06-2025
# Purpose: Solve a Sudoku puzzle.

class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str


    def find_empty_cell(self):
        # Iterates through every digit in a row of the puzzleboard. 
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0) # Find the first instance of '0' (empty cell) in the given row.
                return row, col # Returns coordinates of first empty cell.
            except ValueError: 
                pass
        return None # If no '0' (empty cell) is found, return None

    def valid_in_row(self, row, num):
        return num not in self.board[row] # Returns True if digit is not in the given row.

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9)) # Returns True if digit is not in the given column.

    def valid_in_square(self, row, col, num):
        # Find the index of the top-left 3x3 grid:
        row_start = (row // 3) * 3 
        col_start = (col // 3) * 3
        
        # Iterates through all 9 squares in 3x3 grid:
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False # If digit already exists in 3x3 grid, return False
        return True # Otherwise, return True

    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num) # Verifies validity of num in row
        valid_in_col = self.valid_in_col(col, num) # Verifies validity of num in col
        valid_in_square = self.valid_in_square(row, col, num) # Verifies validity of num in 3x3 grid
        return all([valid_in_row, valid_in_col, valid_in_square]) # Returns True if all three checks are True. Othwise, returns False.

    def solver(self):
        # Checks if all previously empty cells are filled:
        if (next_empty := self.find_empty_cell()) is None:
            return True
        
        # Try all digits 1-9 in empty cell:
        for guess in range(1, 10):

            # If guess passes all three validity checks, insert number to the board:
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess

                # Calls solver() recursively to solve the entire board 
                if self.solver():
                    return True # Once the entire board is solved, return True
                self.board[row][col] = 0 # If a guessed number led to a "dead end," reset cell to 0 and try the next number
        return False # If no guess in the 1-9 range worked, return False

def solve_sudoku(board):
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}') # Print unsolved Sudoku puzzle

    # If solver() returned True, print the solved puzzle:
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}') # Print solved Sudoku puzzle

    # If solver() returned False, puzzle is unsolvable.
    else:
        print('The provided puzzle is unsolvable.')
        
    return gameboard

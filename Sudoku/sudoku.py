# Game to salve sudoku puzzles

def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that's not filled yet --> represnted with -1
    #return row, col tuple (or (None, None) if there is none)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None #if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    #figures out whether the guess at the row/col of the puzzle is a valid guess
    #returns True if is valid, False otherwise

    #check the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    #check the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #check the subgrid
    row_start = (row // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 2 // 3 = 0
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    #step 1: choose some place on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    #step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    #step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        #step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            #step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            #step 4: then we recursively call our solver
            if solve_sudoku(puzzle):
                return True
        #step 5: if not valid OR if our guess does not solve the puzzle, then we need to backtrack and try a new number
        puzzle[row][col] = -1 #reset the guess
    pass

if __name__ == '__main__':
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],
        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],
        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
# Play minesweeper in the terminal

import random

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs 

        #create the board
        self.board = self.make_new_board()#plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        self.dug = set()

    def assign_values_to_board(self):
        # assign a value to each cell in the board
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # iterate through each of the neighboring positions and sum number of bombs
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # our location
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1
        return board

    def dig(self, row, col):
        # dig at that location
        # return True if successful dig, False if bomb dug
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def __str__(self):
        # print the board
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        # put this together in a string
        string_rep = ''
        # get the max column width for printing
        widths = []
        for idx in range(self.dim_size):
            columns = list(zip(*visible_board))[idx]
            widths.append(len(max(columns, key=len)))
        indices = [i for i in range(self.dim_size)]
        indices_width = len(str(max(indices)))
        # print the indices
        indices_row = ' ' * indices_width + ' | ' + ' | '.join([str(i).center(widths[i]) for i in range(self.dim_size)]) + ' |'
        string_rep += indices_row + '\n'
        string_rep += '-' * len(indices_row) + '\n'
        for i in range(len(visible_board)):
            row = str(i).rjust(indices_width) + ' | ' + ' | '.join([str(cell).center(widths[idx]) for idx, cell in enumerate(visible_board[i])]) + ' |'
            string_rep += row + '\n'
        return string_rep
    

def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant bombs
    board = Board(dim_size, num_bombs)

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = input("Where would you like to dig? Input as row, col: ")
        row, col = map(int, user_input.split(','))
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid location. Please try again.")
            continue

        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb
            break #game over
    if safe:
        print("You won!")
    else:
        print("Game over")
        # let's reveal the whole board!
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()

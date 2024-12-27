# Little program to play Tic-Tac-Toe
import random
import math

class Player:
    #select the letter for the player x or o
    def __init__(self, letter):
        self.letter = letter #select the letter for the player x or o


    #next move given the game
    def get_move(self, game):
        pass
    
#class for the human player
class RandomComputerPlayer(Player):
    
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

#Class for human player
class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
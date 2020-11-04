# -*- coding: utf-8 -*-

import numpy as np
import game

class State():

    def __init__(self, board, a, b):

        self.board = np.array(board) #Board configuration
        self.a = a #Player A's remaining pawns
        self.b = b #Player B's remaining pawns



# TODO: create nextState function returning a list of possible next states
def nextState(state):
    sucessors = []

    if (state.a == 0 and state.b == 0): #Game in placing phase
        print("Placing phase")

    else: #Game in moving phase
        print("Moving phase")


#Empty = 0
#Black = 1
#White = 2

initial_state = State([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], 4, 4)
#self.board = np.zeros((5,5), dtype=np.int16) #Initial board configuration


### Examples ###

#Show game board
game.show(initial_state)

#Placing White pawn (v = 2) at (0,0)
game.place(initial_state, 0, 0, 2)

#Show game board
game.show(initial_state)

#Moving pawn at (0,0) to (1,1)
game.move(initial_state, 0, 0, 1, 1)

#Show game board
game.show(initial_state)

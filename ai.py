# -*- coding: utf-8 -*-

import numpy as np
import game

class State():

    def __init__(self, board, a, b):

        self.board = np.array(board) #Board configuration
        self.a = a #Player A's remaining pawns
        self.b = b #Player B's remaining pawns


def nextState(state): #Returns a list of possible next states
    successors = []

    if (state.a != 0 or state.b != 0): #Game in placing phase
        print("\n*** Placing phase ***\n")

        for i in range(5): #Iterating through every cell of the board
            for j in range(5):
                new_state = State(state.board, state.a, state.b - 1) #Substracting 1 pawn to player B (AI)
                game.place(new_state, i, j, 2, False)
                if not (np.array_equal(new_state.board, state.board)):
                    successors.append(new_state)


    else: #Game in moving phase
        print("\n*** Moving phase ***\n")

        for i in range(5): #Iterating through every cell of the board
            for j in range(5):
                if (state.board[i][j] == 2): #If the case contain a player B's pawn
                    adjacentSlots = game.getAdjacent(state, i, j)

                    for p in adjacentSlots:
                        new_state = State(state.board, state.a, state.b)
                        game.move(new_state, i, j, p[0],p[1], False)
                        if not (np.array_equal(new_state.board, state.board)):
                            successors.append(new_state)

    return successors


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
game.place(initial_state, 0, 0, 2, False)

#Show game board
game.show(initial_state)

#Moving pawn at (0,0) to (1,1)
game.move(initial_state, 0, 0, 1, 1, False)

#Show game board
game.show(initial_state)

print("\nPossible next states :")

n = nextState(initial_state)

for i in n: #Printing all the possible next states
    print("\n")
    print(i.board)
    print("\n")

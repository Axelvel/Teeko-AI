# -*- coding: utf-8 -*-

import numpy as np
import game


#Empty = 0
#Black = 1
#White = 2

"""
@desc class of the gameboard
"""
class State():

    def __init__(self, board, a, b,t):

        self.board = np.array(board) #Board configuration
        self.a = a #Player A's remaining pawns
        self.b = b #Player B's remaining pawns
        self.t = t #player's turn  (-1 or 1)

    def switchPlayer(self):
        self.t *= -1

"""
@desc function that searchs for the possible next states
@param State $state - the state of the current board Game
@return array $successors - the list of all the next possible states
"""

def nextState(state): #Returns a list of possible next states
    successors = []

    ###QUAND CEST LIA CEST EGAL A -1
    if (state.t == 1): #Player 1
        x = 1 ##donc 1 ?
        y = 0
    else:       #Player 2
        x = 0
        y = 1 ##donc 1 ?

    if (state.a != 0 or state.b != 0): #Game in placing phase
        #print("\n*** Placing phase ***\n")

        #In the placing phase, we can place a pawn wherever we want except where there are pawns already
        for i in range(5): #Iterating through every cell of the board
            for j in range(5):
                new_state = State(state.board, state.a - x, state.b - y,state.t*-1) #Substracting 1 pawn to player B (AI)
                game.place(new_state, i, j, False)
                if not (np.array_equal(new_state.board, state.board)):
                    successors.append(new_state)


    else: #Game in moving phase
        #print("\n*** Moving phase ***\n")

        for i in range(5): #Iterating through every cell of the board
            for j in range(5):
                if (state.board[i][j] == state.t): #If the case contain a player's pawn
                    adjacentSlots = game.getAdjacent(state, i, j)

                    for p in adjacentSlots:
                        new_state = State(state.board, state.a, state.b,state.t)
                        game.move(new_state, i, j, p[0],p[1], False)
                        if not (np.array_equal(new_state.board, state.board)):
                            successors.append(new_state)

    return successors

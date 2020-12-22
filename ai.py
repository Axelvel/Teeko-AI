# -*- coding: utf-8 -*-

import numpy as np
import game


"""
@desc class of the gameboard
"""
class State():


    def __init__(self, board, a, b, t):


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

def nextState(state):
    successors = []


    if (state.t == 1): #Player 1
        x = 1
        y = 0
    else: #Player 2
        x = 0
        y = 1

    if (state.a != 0 or state.b != 0): #Game in placing phase

        for i in range(5):
            for j in range(5):

                new_state = State(state.board, state.a - x, state.b - y,state.t*-1)

                game.place(new_state, i, j, False)
                if not (np.array_equal(new_state.board, state.board)):
                    successors.append(new_state)

    else:  #Game in moving phase
        for i in range(5):
            for j in range(5):
                if (state.board[i][j] == state.t):
                    adjacentSlots = game.getAdjacent(state, i, j)

                    for p in adjacentSlots:

                        new_state = State(state.board, state.a, state.b,state.t) #Check

                        game.move(new_state, i, j, p[0],p[1], False)
                        if not (np.array_equal(new_state.board, state.board)):
                            successors.append(new_state)

    return successors


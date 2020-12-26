# -*- coding: utf-8 -*-

import game
import ai
import numpy as np

maxSize = float("inf") ##VALUE OF INFINITY

"""
@desc function that calculate the heuristic value for a given state (+inf,-inf or an alternative value)
@param State $state - possible next state
@param int $depth - actual depth of the tree
@return int $value - heuristic value for the state
"""
def eval(state):
    value = 0
    if game.isWinning(state,-state.t):
        value = maxSize * -state.t
    else :
        '''##METHODE 1
            for x in range(5):
                for y in range(5):
                    if state.board[x][y] == state.t:
                        pawnsWeight = stateWeightForPawn(state,x,y)
                        for a in range(5):
                            for b in range(5):
                                if state.board[a][b] == state.t:
                                    value = value + state.t * pawnsWeight[a][b]
        '''
        #METHODE 2
        weights = [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 2, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                    ]
        for x in range(5):
            for y in range(5):
                if state.board[x][y] == state.t or state.board[x][y] == -state.t:
                    value = value + state.board[x][y] * weights[x][y]
    return value

"""
@desc function that creates a 5x5 with the weights of each case, depending on the position of the selected pawn
@param State $state - the state of the current board Game
@param int $x - x coordinates of the selected pawn
@param int $y - y coordinates of the selected pawn
@return array $stateWeight - 5x5 matrice
"""
def stateWeightForPawn(state,x,y):
    stateWeight = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
                ]

    nearPawns = game.getAdjacent(state,x,y)
    for nearPawn in nearPawns:
        stateWeight[nearPawn[0]][nearPawn[1]] = 2

    remotePawnsCoordinates = [[x-1,y-2],[x+1,y-2],[x-1,y+2],[x+1,y+2],[x-2,y-1],[x-2,y+1],[x+2,y-1],[x+2,y+1]]
    for remotePawn in remotePawnsCoordinates:
        if remotePawn[0]>=0 and remotePawn[1]>=0 and remotePawn[0]<=4 and remotePawn[1]<=4:
            stateWeight[remotePawn[0]][remotePawn[1]] = 1

    return stateWeight

"""
@desc function that searches for the best move to take according to the MinMax algorithm
@param State $state - the state of the current board Game
@param int $depth - actual depth of the tree
@return State $besteMove - best next state
"""
def IAbestMove(state,depth):
    bestScore = maxSize
    bestMove = None
    alpha = -maxSize
    beta = maxSize

    nextStates = ai.nextState(state)

    for newState in nextStates:
        score = MinMax(newState,depth,alpha,beta,False)

        if(score < bestScore):
            bestMove = newState
            bestScore = score

    return bestMove

"""
@desc minimax algorithm
@param State $state - the state of the current board Game
@param int $depth - actual depth of the tree
@param bool $maximizing - True to maximize, False to minimize
@return int $bestScore - heuristic value of the the best next state
"""
def MinMax(state,depth,alpha,beta,maximizing):
    if game.isWinning(state,state.t) == True or game.isWinning(state,-state.t) == True or depth == 0:
        return eval(state)

    if maximizing:
        bestScore = -maxSize
        nextStates = ai.nextState(state)

        for newState in nextStates:
            score = MinMax(newState,depth-1,alpha,beta,False)

            bestScore = max(score,bestScore)

            alpha = max(alpha,score)
            if beta <= alpha:
                break

        return bestScore
    else:
        bestScore = maxSize
        nextStates = ai.nextState(state)

        for newState in nextStates:
            score = MinMax(newState,depth-1,alpha,beta,True)

            bestScore = min(score,bestScore)

            beta = min(beta,score)
            if beta <= alpha:
                break

        return bestScore

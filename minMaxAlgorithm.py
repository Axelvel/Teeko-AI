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
def eval(state,depth):
    value = 0
    if game.isWinning(state,1):
        value = 100
    elif game.isWinning(state,-1):
        value = -100
    else :
        for x in range(5):
            for y in range(5):
                if state.board[x][y] == state.t:
                    pawnsWeight = stateWeightForPawn(state,x,y)
                    ###REPARCOURS DE LA matri
                    for a in range(5):
                        for b in range(5):
                            if state.board[a][b] == state.t:
                                value = value + state.t * pawnsWeight[a][b]
    return value + depth
        #SI IL GAGNE PAS, TROUVER UN MOYEN DE CHOISIR UN AUTRE State

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
    ###GET ADJACENTS de x et y, prendre leurs coordonnées et mettre 2 dans state weight
    nearPawns = game.getAdjacent(state,x,y)
    for nearPawn in nearPawns:
        stateWeight[nearPawn[0]][nearPawn[1]] = 2

    remotePawnsCoordinates = [[x-1,y-2],[x+1,y-2],[x-1,y+2],[x+1,y+2],[x-2,y-1],[x-2,y+1],[x+2,y-1],[x+2,y+1]]
    for remotePawn in remotePawnsCoordinates:
        if remotePawn[0]>=0 and remotePawn[1]>=0 and remotePawn[0]<=4 and remotePawn[1]<=4:
            stateWeight[remotePawn[0]][remotePawn[1]] = 1

    return stateWeight

"""
@desc function searches for the best move to take according to the MinMax algorithm
@param State $state - the state of the current board Game
@param int $depth - actual depth of the tree
@return State $besteMove - best next state
"""
def IAbestMove(state,depth):
    bestScore = -maxSize
    bestMove = None

    nextStates = ai.nextState(state)

    #print("Impression des scores de chaques etats suivants :")
    #i = 0
    for newState in nextStates:
        #game.show(newState)
        #print(game.isWinning(newState,-newState.t))
        score = MinMax(newState,depth,False)
        #print("Etat "+str(i)+" : " +str(score))
        #i = i+1
        if(score > bestScore):
            bestMove = newState
            bestScore = score

    return bestMove

"""
@desc function of the minimize and maximize algorithms
@param State $state - the state of the current board Game
@param int $depth - actual depth of the tree
@param bool $maximizing - True to maximize, False to minimize
@return int $bestScore - heuristic value of the the best next state
"""
def MinMax(state,depth,maximizing):
    if game.isWinning(state,state.t) == True or game.isWinning(state,-state.t) == True or depth == 0:
        return eval(state,depth)

    if maximizing:
        bestScore = -maxSize
        nextStates = ai.nextState(state)

        for newState in nextStates:
            score = MinMax(newState,depth-1,False)
            #bestScore = max(score,bestScore)
            if score > bestScore:
                bestScore = score

        return bestScore
    else:
        bestScore = maxSize
        nextStates = ai.nextState(state)

        for newState in nextStates:
            score = MinMax(newState,depth-1,True)
            #bestScore = min(score,bestScore)
            if score < bestScore:
                bestScore = score

        return bestScore

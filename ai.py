# -*- coding: utf-8 -*-

#EVERYTHING CONCERNING THE AI

import numpy as np
import game
import random
import copy
maxSize = float("inf") ##VALUE OF INFINITY


"""
@desc class of the Teeko AI
@param State $board - actual state of the board game
@param int $IAplayer - value indating whose player's turn it is
"""
class TeekoAI:
    def __init__(self, board,IAplayer):
        self.board = board
        self.IAplayer = IAplayer

    """
    @desc function that plays the game in easy mode, making random decisions for the AI.
    """
    def playEasy(self):
        if self.board.remainingPawns != 0:
            while 1:
                x =  random.randint(0,4)
                y =  random.randint(0,4)
                if self.board.place(int(x),int(y),False):
                    break
        else:
            while 1:
                x =  random.randint(0,4)
                y =  random.randint(0,4)
                a =  random.randint(0,4)
                b = random.randint(0,4)
                if self.board.move(int(x),int(y),int(a),int(b),False):
                    break

    """
    @desc function that plays the game in medium or hard mode, depending on the value of 'mode' given
    @param int $depth - depth of the current state in the minimax algorithm
    @param int $mode - mode of the game (0 for intermediate, 1 for hard)
    @return State $bestState - best next move for the IA to take
    """
    def playMediumOrHard(self,depth,mode):

        player = self.board.playerPlaying
        bestScore = maxSize * -player
        tempScore = 0
        alpha = -maxSize
        beta = maxSize

        #Temporary board for testing each child
        tempState = copy.deepcopy(self.board)
        bestState = None

        if self.board.remainingPawns != 0:
            for x in range(5):
                for y in range(5):
                    if tempState.place(x,y,False):
                        if player == -1:
                            tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,False)
                            if tempScore <= bestScore:
                                bestScore = tempScore
                                bestState = tempState
                        elif player == 1:
                            tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,True)
                            if tempScore >= bestScore:
                                bestScore = tempScore
                                bestState = tempState
                        tempState = copy.deepcopy(self.board)
        else:
            for x in range(5):
                for y in range(5):
                    adjacents = tempState.getAdjacent(x,y)

                    for adjacent in adjacents:
                        if tempState.move(x,y,adjacent[0],adjacent[1],False):
                            if player == -1:
                                tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,False)
                                if tempScore <= bestScore:
                                    bestScore = tempScore
                                    bestState = tempState
                            elif player == 1:
                                tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,True)
                                if tempScore >= bestScore:
                                    bestScore = tempScore
                                    bestState = tempState
                            tempState = copy.deepcopy(self.board)

        self.board = bestState
        return bestState

    """
    @desc minimax function
    @param int $mode - mode of the game (0 for intermediate, 1 for hard)
    @param State $childState - state of the board for each child
    @param int $depth - depth of the current state in the minimax algorithm
    @param int $alpha,beta - value used for the alpha beta pruning
    @param bool $isMaximizing - allows the minimax to know when to maximize or minimize
    @return int $bestScore - the best score pulled up from the algorithm
    """
    def minimax(self,mode,childState,depth,alpha,beta,isMaximizing):

        if childState.winner() != 0 or depth ==0:
            return self.eval(childState,depth,mode)

        if isMaximizing:
            bestScore = -maxSize
            tempScore = 0

            tempState = copy.deepcopy(childState)

            if tempState.remainingPawns != 0:
                for x in range(5):
                    for y in range(5):
                        if tempState.place(x,y,False):
                            tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,False)
                            alpha = tempScore

                            if tempScore >= bestScore:
                                bestScore = tempScore
                            if alpha >= beta:
                                return alpha
                            tempState = tempState = copy.deepcopy(childState)

            else:
                for x in range(5):
                    for y in range(5):
                        adjacents = tempState.getAdjacent(x,y)

                        for adjacent in adjacents:
                            if tempState.move(x,y,adjacent[0],adjacent[1],False):

                                tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,False)
                                alpha = tempScore

                                if tempScore >= bestScore:
                                    bestScore = tempScore
                                if alpha >= beta:
                                    return alpha
                                tempState = tempState = copy.deepcopy(childState)
            return bestScore
        else:
            bestScore = maxSize
            tempScore = 0

            tempState = tempState = copy.deepcopy(childState)

            if tempState.remainingPawns != 0:
                for x in range(5):
                    for y in range(5):
                        if tempState.place(x,y,False):
                            tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,True)
                            beta = tempScore

                            if tempScore <= bestScore:
                                bestScore = tempScore
                            if alpha >= beta:
                                return beta
                            tempState = tempState = copy.deepcopy(childState)

            else:
                for x in range(5):
                    for y in range(5):

                        adjacents = tempState.getAdjacent(x,y)
                        for adjacent in adjacents:
                            if tempState.move(x,y,adjacent[0],adjacent[1],False):

                                tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,True)
                                beta = tempScore
                                if tempScore <= bestScore:
                                    bestScore = tempScore
                                if alpha >= beta:
                                    return beta
                                tempState = tempState = copy.deepcopy(childState) 
            return bestScore

    """
    @desc function eval, giving value to the boards when a winning combination is found or when depth has reached 0
    @param State $childState - state of the board
    @param int $depth - depth of the current state in the minimax algorithm
    @param int $mode - mode of the game (0 for intermediate, 1 for hard)
    @return int $value - the score of the board
    """
    def eval(self,state,depth,mode):
        if state.winner()!=0:
            return maxSize * state.winner()
        else:
            value = 0
            if mode == 0: ##MEDIUM LEVEL
                for x in range(5):
                    for y in range(5):
                        if state.board[x][y] != 0:
                            pawnsWeight = self.stateWeightForPawn(state,x,y)
                            for a in range(5):
                                for b in range(5):
                                    if state.board[a][b] != 0:
                                        value = value + state.board[a][b] * pawnsWeight[a][b]
                return value
            elif mode == 1: ##HARD LEVEL
                boardWeights = [
                            [0, 1, 0, 1, 0],
                            [1, 2, 2, 2, 1],
                            [0, 2, 3, 2, 0],
                            [1, 2, 2, 2, 1],
                            [0, 1, 0, 1, 0]
                            ]
                for x in range(5):
                    for y in range(5):
                        if state.board[x][y] != 0:
                            value = value + state.board[x][y] * boardWeights[x][y]

                return value

    """
    @desc function creating the weights of the pawn surrounding a chosen pawn
    @param State $childState - state of the board
    @param int $x,y - coordinates of the chosen pawn
    @return array $stateWeight - weights of the emplacements near the pawn
    """
    def stateWeightForPawn(self,state,x,y):
        stateWeight = [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                    ]

        nearPawns = state.getAdjacent(x,y)
        for nearPawn in nearPawns:
            stateWeight[nearPawn[0]][nearPawn[1]] = 2

        remotePawnsCoordinates = [[x-1,y-2],[x+1,y-2],[x-1,y+2],[x+1,y+2],[x-2,y-1],[x-2,y+1],[x+2,y-1],[x+2,y+1]]
        for remotePawn in remotePawnsCoordinates:
            if remotePawn[0]>=0 and remotePawn[1]>=0 and remotePawn[0]<=4 and remotePawn[1]<=4:
                stateWeight[remotePawn[0]][remotePawn[1]] = 1

        return stateWeight

# -*- coding: utf-8 -*-

#EVERYTHING CONCERNING THE AI

import numpy as np
import game
import random
import copy
maxSize = float("inf") ##VALUE OF INFINITY

class TeekoAI:
    def __init__(self, board,IAplayer):
        self.board = board
        self.IAplayer = IAplayer #Id of the IA, useful when there are two different ai (in human vs ia, always at -1)

    def playEasy(self):
        if self.board.remainingPawns != 0:
            while 1:
                x =  random.randint(0,4)
                y =  random.randint(0,4)
                if self.board.place(int(x),int(y),False):
                    break
        else: #if game in moving phase
            while 1:
                x =  random.randint(0,4)
                y =  random.randint(0,4)
                a =  random.randint(0,4)
                b = random.randint(0,4)
                if self.board.move(int(x),int(y),int(a),int(b),False):
                    break

    def playMediumOrHard(self,depth,mode):##MINIMAX

        player = self.board.playerPlaying
        bestScore = maxSize * -player ##start from the worse score
        tempScore = 0
        alpha = -maxSize
        beta = maxSize

        #board temporaire pour les test
        tempState = copy.deepcopy(self.board)
        bestState = None

        if self.board.remainingPawns != 0: #if game in placing phase
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
                        tempState = copy.deepcopy(self.board) #remise a 0
                        #print(tempScore)

        else: #if game in moving phase
            for x in range(5):
                for y in range(5):
                    ###POUR CHAQUE PION, ON RECUP LES ADJACENTS ET ON BOUGE LA
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
                            tempState = copy.deepcopy(self.board) #remise a 0
                            #print(tempScore)

        print("The best score found was "+str(bestScore))
        self.board = bestState #apply the change to both
        return bestState

    def minimax(self,mode,childState,depth,alpha,beta,isMaximizing):
        ##SI ON RENCONTRE UN ETAT GAGNANT OU SI DEPTH EST EPUISE, ON DONNE UNE VALEUR A LA BOARD
        if childState.winner() != 0 or depth ==0:
            return self.eval(childState,depth,mode)

        #Si on veut maximiser, alors on commencer à -inf, pour se rapprocher de inf
        #Pour se faire on crée de nouveau des fils, et pour chaque fils on relancer minimax mais avec min d'active
        #De cette manière onfinit par arriver sur un etat gagnant qui renvoie le score et le fait remonter
        #On choisit ensuite le meilleur parmi tout ceux qui sont remontes, et c'est celui qu'on renvoie

        if isMaximizing:
            bestScore = -maxSize
            tempScore = 0

            tempState = copy.deepcopy(childState)

            if tempState.remainingPawns != 0: #if game in placing phase
                for x in range(5):
                    for y in range(5):
                        if tempState.place(x,y,False):
                            #on lance min
                            tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,False)
                            alpha = tempScore

                            if tempScore >= bestScore:
                                bestScore = tempScore
                            if alpha >= beta:
                                return alpha
                            tempState = tempState = copy.deepcopy(childState) #remise a 0

            else: #if game in moving phase
                for x in range(5):
                    for y in range(5):
                        ###POUR CHAQUE PION, ON RECUP LES ADJACENTS ET ON BOUGE LA
                        adjacents = tempState.getAdjacent(x,y)
                        for adjacent in adjacents:
                            if tempState.move(x,y,adjacent[0],adjacent[1],False):

                                #on lance min
                                tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,False)
                                alpha = tempScore

                                if tempScore >= bestScore:
                                    bestScore = tempScore
                                if alpha >= beta:
                                    return alpha
                                tempState = tempState = copy.deepcopy(childState) #remise a 0
            return bestScore
        else: #isMinimizing
            #Si on veut minimiser, alors on commencer à inf, pour se rapprocher de -inf
            #Pour se faire on crée de nouveau des fils, et pour chaque fils on relancer minimax mais avec max d'active
            #De cette manière onfinit par arriver sur un etat gagnant qui renvoie le score et le fait remonter
            #On choisit ensuite le meilleur parmi tout ceux qui sont remontes, et c'est celui qu'on renvoie
            bestScore = maxSize
            tempScore = 0

            tempState = tempState = copy.deepcopy(childState)

            if tempState.remainingPawns != 0: #if game in placing phase
                for x in range(5):
                    for y in range(5):
                        if tempState.place(x,y,False):
                            #on lance min
                            tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,True)
                            beta = tempScore

                            if tempScore <= bestScore:
                                bestScore = tempScore
                            if alpha >= beta:
                                return beta
                            tempState = tempState = copy.deepcopy(childState) #remise a 0

            else: #if game in moving phase
                for x in range(5):
                    for y in range(5):
                        ###POUR CHAQUE PION, ON RECUP LES ADJACENTS ET ON BOUGE LA
                        adjacents = tempState.getAdjacent(x,y)
                        for adjacent in adjacents:
                            if tempState.move(x,y,adjacent[0],adjacent[1],False):

                                #on lance min
                                tempScore = self.minimax(mode,tempState,depth-1,alpha,beta,True)
                                beta = tempScore
                                if tempScore <= bestScore:
                                    bestScore = tempScore
                                if alpha >= beta:
                                    return beta
                                tempState = tempState = copy.deepcopy(childState) #remise a 0
            return bestScore

    def eval(self,state,depth,mode):
        if state.winner()!=0:
            return maxSize * state.winner()
        else:
            value = 0
            if mode == 0: ##MEDIUM LEVEL
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
            elif mode == 1: ##HARD LEVEL
                for x in range(5):
                    for y in range(5):
                        if state.board[x][y] != 0:
                            pawnsWeight = self.stateWeightForPawn(state,x,y)
                            for a in range(5):
                                for b in range(5):
                                    if state.board[a][b] != 0:
                                        value = value + state.board[a][b] * pawnsWeight[a][b]

                return value

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

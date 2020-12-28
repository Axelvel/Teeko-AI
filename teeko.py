# -*- coding: utf-8 -*-

import gameBoard
import ai

state = gameBoard.boardGame([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],1,8)

ai = ai.TeekoAI(state,-1)

state.print()
while(state.winner()==0):

    state.playPlayer()
    state.print()
    state = ai.playHard(3)
    state.print()

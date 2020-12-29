# -*- coding: utf-8 -*-

import game
import ai

state = game.boardGame([
            [0, 1, -1, 0, 0],
            [0, 0, 0, 0, -1],
            [0, 1, -1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, -1]
        ],1,0)

ai = ai.TeekoAI(state,-1)

state.print()
while(state.winner()==0):

    state.playPlayer()
    state.print()
    state = ai.playMediumOrHard(3,int(1)) #play hard here. 0 for intermediate.
    state.print()

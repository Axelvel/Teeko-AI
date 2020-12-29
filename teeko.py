# -*- coding: utf-8 -*-

import game
import ai
import argparse



parser = argparse.ArgumentParser(description='Teeko Game')
parser.add_argument("-c", "--cli", action = "store_true", help="Launch program into CLI mode")
args = parser.parse_args()


if (args.cli == True):

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

        state.playPlayer() ## TODO: check for player inputs
        state.print()
        state = ai.playMediumOrHard(3,int(1)) #play hard here. 0 for intermediate.
        state.print()
else:
    exec(open("ui.py").read())

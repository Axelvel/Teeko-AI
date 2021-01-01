# -*- coding: utf-8 -*-

import game
import ai
import argparse

#Argument parser for --cli
parser = argparse.ArgumentParser(description='Teeko Game')
parser.add_argument("-c", "--cli", action = "store_true", help="Launch program into CLI mode")
args = parser.parse_args()


if (args.cli == True): #If CLI mode is detected

    #initialize gameBoard
    state = game.boardGame([
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ], 1, 8)

    ai = ai.TeekoAI(state,-1)

    state.print()
    print("\n")

    while(state.winner() == 0):
        state.playPlayer()
        state.print()
        state = ai.playMediumOrHard(3,int(1)) #Play hard here. 0 for intermediate.
        state.print()

    print("Game finished!\n")
    if (state.winner() == 1):
        print("Congrats, you have won this game!\n")
    else:
        print("Booo, you lost :(")

else: #If UI mode is detected
    exec(open("ui.py").read()) #Launch ui.py script

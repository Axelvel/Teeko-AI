# -*- coding: utf-8 -*-

import game
from ai import *
import numpy
"""
initial_state = State([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], 4, 4)
"""
initial_state = State([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], 4, 4)
print("\nWelcome to our Teeko game!\n")

print("Select game mode:\n")
print("     - P vs P\n")
print("     - P vs AI\n")
print("     - AI vs AI\n")

game.play(initial_state)

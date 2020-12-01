# -*- coding: utf-8 -*-

import os
import time

def place(state, a, b, v, cflag):
    if (state.board[a][b] != 0): #Position is occupied by another pawn
        if (cflag):
            print("This position is occupied. \n")
        return False
    else: #Position is not occupied
        state.board[a][b] = v #We assign the value of the pawn to this position
        return True

def move(state, a, b, x, y, cflag):
    if (a != x or b != y): #Position and destionation must be different
        if (state.board[x][y] != 0): #Destination position is occupied by another pawn
            if (cflag):
                print("This destination is occupied. \n")
            return False
        else: #Destination position is unoccupied
            if (state.board[a][b] == 0): #Initial position is unoccupied
                if (cflag):
                    print("There is no pawn to move at this position. \n")
                return False
            else: #initial position is unoccupied
                adjacentSlots = getAdjacent(state, a, b)
                if [x,y] in adjacentSlots:
                    state.board[x][y] = state.board[a][b] #Moving pawn value
                    state.board[a][b] = 0 #Resetting initial position value to 0 (empty)
                    return True
                else:
                    if (cflag):
                        print("Destination is not adjacent to the selected pawn. \n")
                    return False
    else:
        if (cflag):
            print("Initial position and destination must be different. \n")
        return False

def getAdjacent(state, a, b): #Returns list of adjacent slots
    adjacentSlots = []
    directions = [
        [-1, -1], [-1, 0], [-1, +1],
        [0, -1],           [0, +1],
        [+1, -1], [+1, 0], [+1, +1],
    ]

    for i in directions:
        x = a + i[0]
        y = b + i[1]

        if( 0 <= x <= 4 and 0 <= y <= 4):
            adjacentSlots.append([x,y])

    return adjacentSlots

def show(state): #Show the game board at a given state
    print("\n")
    print(state.board)
    print("\n")

def play(state):
    print("Lauching game...\n")

    i = 0
    t = 0

    while (i != 10): //Nombre total de tours
        os.system('clear')
        print("\n*** Tour " + str(i) + " ***", flush=True)

        show(state)


        if (t == 0): #Player 1's turn
            print("\nPlayer 1's turn\n", flush=True)

            if (state.a != 0): #Placement phase
                print("Placement phase: ")

                while True:
                    try:
                        x_pos = int(input("Choose x position: "))
                        y_pos = int(input ("Choose y position: "))

                    except:
                        print("Sorry, I didn't understand that.")
                        continue

                    if not(0 <= x_pos <= 4 and 0 <= y_pos <= 4):
                        print("Please select values from 0 to 4.")
                        continue

                    if (place(state, x_pos, y_pos, 1, True) == False):
                        continue
                    else:
                        break

                state.a -= 1

                show(state)

                print("Next turn...")
                time.sleep(3)

            else:
                print("Moving phase: ")

                while True:
                    try:
                        x_pos = int(input("Choose x position: "))
                        y_pos = int(input ("Choose y position: "))

                        a_pos = int(input("Choose a position: "))
                        b_pos = int(input ("Choose b position: "))

                    except:
                        print("Sorry, I didn't understand that.")
                        continue

                    if not(0 <= x_pos <= 4 and 0 <= y_pos <= 4 and 0 <= a_pos <= 4 and 0 <= b_pos <= 4 ):
                        print("Please select values from 0 to 4.")
                        continue

                    if (move(state, x_pos, y_pos, a_pos, b_pos, True) == False):
                        continue
                    else:
                        break


                show(state)
                print("Next turn...")
                time.sleep(3)

        else: # Player 2's turn
            print("\nPlayer 2's turn\n", flush=True)

        t = not(t)

        i += 1

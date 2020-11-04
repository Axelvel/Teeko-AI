# -*- coding: utf-8 -*-

def place(state, a, b, v):
    if (state.board[a][b] != 0): #Position is occupied by another pawn
        print("This position is occupied. \n")
    else: #Position is not occupied
        state.board[a][b] = v #We assign the value of the pawn to this position

def move(state, a, b, x, y):
    if (a != x or b != y): #Position and destionation must be different
        if (state.board[x][y] != 0): #Destination position is occupied by another pawn
            print("This destination is occupied. \n")
        else: #Destination position is unoccupied
            if (state.board[a][b] == 0): #Initial position is unoccupied
                print("There is no pawn to move at this position. \n")
            else: #initial position is unoccupied
                state.board[x][y] = state.board[a][b] #Moving pawn value
                state.board[a][b] = 0 #Resetting initial position value to 0 (empty)
    else:
        print("Initial position and destination must be different. \n")

# TODO: create getAdjacent function returning a list of the positions of the adjacent slots
def getAdjacent(state, a, b):
    adjacentSlots = []

    return adjacentSlots

def show(state):
    print("\n")
    print(state.board)
    print("\n")

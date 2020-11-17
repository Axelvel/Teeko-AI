# -*- coding: utf-8 -*-

"""
@desc function that places a pawn on the board
@param State $state - the state of the current board Game
@param int $a,b - the coordinates of the position on which we want to place the pawn
@param int $v - the value of the pawns (0 : empty slot, 1 : black pawn, 2 : white pawn)
@param ? $cflag - ?
"""

def place(state, a, b, v, cflag):
    if (state.board[a][b] != 0): #Position is occupied by another pawn
        if (cflag):
            print("This position is occupied. \n")
    else: #Position is not occupied
        state.board[a][b] = v #We assign the value of the pawn to this position

"""
@desc function that moves a pawn on the board
@param State $state - the state of the current board Game
@param int $a,b - the coordinates of the previous position of the pawns
@param int $a,b - the coordinates of the wanted position of the pawns
@param ? $cflag - ?
"""

def move(state, a, b, x, y, cflag):
    if (a != x or b != y): #Position and destionation must be different
        if (state.board[x][y] != 0): #Destination position is occupied by another pawn
            if (cflag):
                print("This destination is occupied. \n")
        else: #Destination position is unoccupied
            if (state.board[a][b] == 0): #Initial position is unoccupied
                if (cflag):
                    print("There is no pawn to move at this position. \n")
            else: #initial position is unoccupied
                adjacentSlots = getAdjacent(state, a, b)
                if [x,y] in adjacentSlots:
                    state.board[x][y] = state.board[a][b] #Moving pawn value
                    state.board[a][b] = 0 #Resetting initial position value to 0 (empty)
                else:
                    if (cflag):
                        print("Destination is not adjacent to the selected pawn. \n")
    else:
        if (cflag):
            print("Initial position and destination must be different. \n")

"""
@desc function that searchs for the adjacents slots of a pawn
@param State $state - the state of the current board Game
@param int $a,b - the coordinates of the position of the pawn
@return array $adjacentsSlots - list of adjacents slots, described as an array of two int
"""

def getAdjacent(state, a, b):
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

'''
@desc TEST function that searchs for all possible winning combinations. it takes into account the pawns already on the board
@param State $state - the state of the current board Game
@param int $player - the player for which we are searching winning combinations
@return array $winnigCombinations - list of game state in which the player is winning
'''
def winningCombinations(state,player):
    #Serach for all horizontal positions, then vertical, then diagonal, then squares ? and store them into an array
    winning = [];


    blankBoard =[[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
    #Search for all possible combinations, disregarding the actual state of the gameboard
    #vertical

    start_line = 0;
    for i in range(4):
        for j in range(3):
            newBoard = [blankBoard]
            newBoard[i+start_line][j]=1
            show(newBoard)
            winning.append(newBoard)

    return winning


    #compare thoses combinations to the state of the gameboard and only keep the relevants one
    #blablabla

"""
@desc print the gameboard
@param State $state - the state of the current board Game
"""

def show(state): #Show the game board at a given state
    print("\n")
    print(state.board)
    print("\n")

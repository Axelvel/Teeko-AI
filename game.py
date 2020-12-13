# -*- coding: utf-8 -*-


"""
@desc function that places a pawn on the board
@param State $state - the state of the current board Game
@param int $a,b - the coordinates of the position on which we want to place the pawn
@param int $v - the value of the pawns (0 : empty slot, 1 : black pawn, 2 : white pawn)
@param ? $cflag - ?
"""

def place(state, a, b, cflag):
    if (state.board[a][b] != 0): #Position is occupied by another pawn
        if (cflag):
            print("This position is occupied. \n")
        return False
    else: #Position is not occupied
        state.board[a][b] = state.t #We assign the value of the pawn to this position
        state.t *= -1
        return True
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
            return False
        else: #Destination position is unoccupied
            if (state.board[a][b] == 0): #Initial position is unoccupied
                if (cflag):
                    print("There is no pawn to move at this position. \n")
                return False
            else: #initial position is unoccupied
                if (state.board[a][b] == state.t):
                    adjacentSlots = getAdjacent(state, a, b)
                    if [x,y] in adjacentSlots:
                        state.board[x][y] = state.board[a][b] #Moving pawn value
                        state.board[a][b] = 0 #Resetting initial position value to 0 (empty)
                        state.t *= -1
                        return True
                    else:
                        if (cflag):
                            print("Destination is not adjacent to the selected pawn. \n")
                        return False
                else:
                    print("The pawn selected is not one of yours")
                    return False
    else:
        if (cflag):
            print("Initial position and destination must be different. \n")
        return False

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
A AMELIORER
@desc function that verify if the board owns a winning combination
@param State $state - the state of the current board Game
@param int $player - number of the player for which we are checking the boardd
@return bool - whether the board has a winning combination
'''
def isWinning(state,player):
    ##We browse the board from left to right and top to bottom

    #Looking for the first iteration of the pawn with the value of player, and saving its position in posX and posY
    x = 0
    y = 0
    posX = 0
    posY = 0

    while state.board[x][y] != player:
        for x in range(5):
            for y in range(5):
                if state.board[x][y] == player:
                    posX = x
                    posY = y
                    break
            if state.board[x][y] ==player:
                break
        if state.board[x][y] == player:
            #print(state.board[x][y])
            break


    ##HORIZONTAL PAWNS TEST
    compte = 0
    for i in range(posY,5):
        if state.board[x][y] == player:
            y = y + 1
            compte = compte + 1
        else:
            break
    if(compte == 4):
        return True

    ##VERTICAL PAWNS TEST
    x = posX
    y = posY
    compte = 0
    for i in range(posX,5):
        if state.board[x][y] == player:
            compte = compte + 1
            x = x + 1
        else:
            break
    if(compte == 4):
        return True

    ##RIGHT DIAGONAL TEST
    x = posX
    y = posY
    compte = 0
    for i in range(posY,5):
        if state.board[x][y] == player:
            compte = compte + 1
            x = x + 1
            y = y + 1
        else:
            break
        if x > 4:
            break
    if(compte == 4):
        return True

    ##LEFT DIAGONAL TEST
    x = posX
    y = posY
    compte = 0
    for i in range(posX,5):
        if state.board[x][y] == player:
            compte = compte + 1
            x = x + 1
            y = y - 1
        else:
            break
        if y > 4:
            break
    if(compte == 4):
        return True

    ##CUBE TEST
    x = posX
    y = posY
    compte = 0
    directions = [[0,+1],[+1,0],[0,-1],[0,0],]

    if x<4 and y<4 :
        for i in directions:
            if state.board[x][y] == player:
                compte = compte + 1
                x = x + i[0]
                y = y + i[1]
            else:
                break
        if(compte == 4):
            return True

    return False

"""
@desc print the gameboard
@param State $state - the state of the current board Game
"""

def show(state): #Show the game board at a given state
    print("\n")
    print(state.board)
    print("\n")

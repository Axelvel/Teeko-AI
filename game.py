# -*- coding: utf-8 -*-

#BASIC FUNCTIONS OF THE BOARD SUCH AS MOVEMENT ON THE BOARD ETC

import numpy as np


"""
@desc class of te game's board
@param numpyArray $board - matric representing the board
@param int $playerPlaying - value indating whose player's turn it is (1 or -1)
@param int $remainingPawns - pawns left to place on the board (initizalized at 8, 4 for each player)
"""
class boardGame:
    def __init__(self, board, player, n):
        self.board = np.array(board)
        self.playerPlaying = player
        self.remainingPawns = n

    """
    @desc print the game's board.
    """
    def print(self):
        print("\n")
        print(self.board)
        print("\nPlayer "+str(-self.playerPlaying)+" juste played. Turn for "+str(self.playerPlaying)+".\n")

    """
    @desc initizalize the game's board with all zeros.
    """
    def initialize(self):
        self.board = np.zeros((5,5), dtype=np.int16)
        self.playerPlaying = 1
        self.remainingPawns = 8

    """
    @desc switches the player value from 1 to -1 or from -1 to 1
    """
    def switchPlayer(self):
        self.playerPlaying *= -1

    """
    @desc places a pawn on the board
    @param int $x,y - coordinates of the position on which we want to place the pawn
    @param bool $cflag - allowing console messages or not
    @return bool - False if the operation failed, True if it worked
    """
    def place(self,x,y,cflag):
        if (self.board[x][y] != 0): #Position is occupied by another pawn
            if (cflag):
                print("This position is occupied. \n")
            return False
        else:
            self.board[x][y] = self.playerPlaying
            self.remainingPawns -= 1
            self.switchPlayer()
            return True

    """
    @desc places a pawn on the board
    @param int $x,y - coordinates of the pawn we want to move
    @param int $a,b - coordinates of the position on which we want to place the pawn
    @param bool $cflag - allowing console messages or not
    @return bool - False if the operation failed, True if it worked
    """
    def move(self,x,y,a,b,cflag):
        if (a != x or b != y): #Position and destionation must be different
            if (self.board[a][b] != 0): #Destination position is occupied by another pawn
                if (cflag):
                    print("This destination is occupied. \n")
                return False
            else: #Destination position is unoccupied
                if (self.board[x][y] == 0): #Initial position is unoccupied
                    if (cflag):
                        print("There is no pawn to move at this position. \n")
                    return False
                else:
                    if (self.board[x][y] == self.playerPlaying):
                        adjacentSlots = self.getAdjacent(x, y)
                        if [a,b] in adjacentSlots:
                            self.board[a][b] = self.board[x][y]
                            self.board[x][y] = 0
                            self.switchPlayer()
                            return True
                        else:
                            if (cflag):
                                print("Destination is not adjacent to the selected pawn. \n")
                            return False
                    else:
                        if(cflag):
                            print("The pawn selected is not one of yours")
                        return False
        else:
            if (cflag):
                print("Initial position and destination must be different. \n")
            return False


    """
    @desc look for all the positions adjacents to one pawn
    @param int $x,y - coordinates of the pawn
    @return array $adjacentsSlots - array of the position's coordinates
    """
    def getAdjacent(self, a, b):
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

    """
    @desc search for a winning combination
    @return int - value of the player (1 or -1) or 0 when there's none
    """
    def winner(self):
        x = 0
        y = 0
        posX = 0
        posY = 0

        #LINES
        for i in range(5):
            if np.sum(self.board[i] == 1) == 4:
                if np.all(self.board[i][0:4] == 1) or np.all(self.board[i][1:5] == 1):
                    return 1
            elif np.sum(self.board[i] == -1) == 4:#
                if np.all(self.board[i][0:4] == -1) or np.all(self.board[i][1:5] == -1):
                    return -1

        #COLUMNS
        for i in range(5):
            column = self.board[:,i]
            if np.sum(column == 1) == 4:
                if np.all(column[0:4] == 1) or np.all(column[1:5] == 1):
                    return 1
            elif np.sum(column == -1) == 4:
                if np.all(column[0:4] == -1) or np.all(column[1:5] == -1):
                    return -1


        #DIAGONALS
        for i in range(-1,2):
            diag = self.board.diagonal(i)
            oppdiag = np.fliplr(self.board).diagonal(i)

            if np.sum(diag == 1) == 4 or np.sum(oppdiag == 1) == 4:
                if np.all(diag[0:4] == 1) or np.all(oppdiag[0:4] == 1):
                    return 1
                if len(diag)>4:
                    if np.all(diag[1:5] == 1) or np.all(oppdiag[1:5] == 1):
                        return 1
            elif np.sum(diag == -1) == 4 or np.sum(oppdiag == -1) == 4:
                if np.all(diag[0:4] == -1) or np.all(oppdiag[0:4] == -1):
                    return -1
                if len(diag)>4:
                    if np.all(diag[1:5] == -1) or np.all(oppdiag[1:5] == -1):
                        return -1

        #CUBES
        for i in range(4):
            for j in range(4):
                c = [self.board[i][j:j+2],self.board[i+1][j:j+2]]
                cube = np.array(c)

                if np.all(cube == 1):
                    return 1
                elif np.all(cube == -1):
                    return -1

        return 0

    """
    @desc allows the player to play in the console
    """
    def playPlayer(self):
        #If game in placing phase
        if self.remainingPawns != 0:
            while 1:
                print("Enter the coordinates of the pawn you wish to place.")
                x = input()
                y = input()
                if self.place(int(x),int(y),True):
                    break
        else: #if game in moving phase
            while 1:
                print("Enter the coordinates of the pawn you wish to move.")
                x = input()
                y = input()
                print("Enter the coordinates of the place you wish to place it.")
                a = input()
                b = input()
                if self.move(int(x),int(y),int(a),int(b),True):
                    break

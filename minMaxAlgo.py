from sys import maxSize

###Algorithme min-max, qui permet à l'IA de sélectionner les meilleurs déplacements

##i_depth represents how deep we are into the tree (we start at a
#certain velue, then at every iteration we decrease that value
#until we reach 0)
##i_value is the heuristic value of the game
class Node(object):
    def __init__ (self,i_depth,i_playerNum,i_board,i_value=0):
        self.i_depth = i_depth
        self.i_playerNum = i_playerNum
        self.i_gameState = i_board
        self.i_value = i_value
        self.children = []
        self.CreateChildren()

    def CreateChildren(self):
        if self.i_depth >= 0:
            #Create all differents moves of a certain player
            #So we take the actuel state of the game and use the nextState function
            #puis on append le tout dans children
            #pour ça, on crée un node avec depth-1, le num du joueur adverse et realVal
            #si value de realVal est 0, le joueur a gagne. si c'est négatif, il a perdu
            print("hola")

    def RealVal(self,value):
        if(value == 0): #If the player has won
            return maxSize * self.i_playerNum
        elif(value < 0):
            return maxSize * -self.i_playerNum
        return 0

'''
@desc algorithm on min max
@param Node $node - node on which we are actually
@param int $i_depth - depth of the tree at this emplacement
@param int $iplayerNum - number of the player on this level
@return i_bestValue - the best next state to go to according to the algorithm
'''
def MinMax(node, i_depth, i_playerNum):
    #Si on est au bout de l'arbre ou si on a atteint un état gagnant
    if(i_depth == 0) or (abs(node.i_value)==maxSize):
        return node.i_value ##Alors on retourne la valeur de ce node au parent (comme ça on sait quel est le chemin le plus efficace)

    i_bestValue = maxSize * -i_playerNum
    for child in node.children:
        ##récursivité sur tous les enfants de node. on récupère dans i_val la valeur obtenue au dessus
        i_val = MinMax(child,i_depth-1,-i_PlayerNum)
        ##checking the distance of where we want to be from where we currently are with this current child
        #en gros on regarde quel node le plus proche nous fait gagner, et on récupère sa valeur
        if(abs(maxSize * i_playerNum - i_val) < abs(maxSize * i_playerNum - i_bestValue)):
            i_bestValue = i_val

        return i_bestValue ##value of the node of the best movement to make

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
    poxY = 0
    while state.board[x][y] != player:
        for x in range(5):
            for y in range(5):
                if state.board[x][y] == player:
                    posX = x
                    posY = y
                    break
            if state.board[x][y] == player:
                break
        if state.board[x][y] == player:
            print(state.board[x][y])
            break


    ##HORIZONTAL PAWNS TEST
    compte = 0
    for i in range(posY,5):
        if state.board[x][y] == player :
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
        if state.board[x][y] == player :
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
        if state.board[x][y] == player :
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
        if state.board[x][y] == player :
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

    for i in directions:
        if state.board[x][y] == player :
            compte = compte + 1
            x = x + i[0]
            y = y + i[1]
        else:
            break
    if(compte == 4):
        return True

    return False

'''DEBUT DU PROGRAMME'''
##ceci doit être dans le main, là c'est juste du brouillon
i_curPlayer = 1
i_depth = 4

while(THE GAME IS ON):
    ##un joueur joue, on enregistre son mouvement
    if not(isWinning(state,i_curPlayer)):
        ##si le joueur n'a pas gagné, on switch à l'ia'
        i_curPlayer *= -1
        ##Après on crée l'arbre
        node = Node(i_depth,i_curPlayer,state,0)
        #bestChoice = node ayant la valeur de la board pour le meilleur mouvement
        i_bestValue = -i_curPlayer * maxSize

        ##determine what movement to make
        for n_child in node.children:
            i_val = MinMax(n_child,i_depth,-icurPlayer)
            if(abs(maxSize * i_curPlayer - i_val) < abs(maxSize * i_curPlayer - i_bestValue)):
                i_bestValue = i_val
                bestChoice = n_child
        bestChoice += 1

        print("print the choice of the computer here")
        ##Faire les modifications nécessaires sur la stateboard
        isWinning(state,i_curPlayer)
        i_curPlayer *= -1

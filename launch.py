import ai
import game
import minMaxAlgorithm

test_state = ai.State([
            [0, 0, -1, 0, -1],
            [0, -1, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [1, 1, 0, 0, -1],
            [0, 0, 0, 0, 0]
        ], 0, 0, 1)

depth = 2


while(not(game.isWinning(test_state,-1)) and not(game.isWinning(test_state,1))):
    game.show(test_state)
    print("Quel pion voulez-vous bouger ? Donnez les coordonnées x et y")
    a = input()
    b = input()
    print("Vous voulez bouger le pion "+str(a)+"/"+str(b)+". Ou voulez-vous le bouger")
    x = input()
    y = input()
    game.move(test_state,int(a),int(b),int(x),int(y),False)
    print("Etat actuel de la board : ")
    game.show(test_state)

    print("Au tour de l'ia...")
    test_state = minMaxAlgorithm.IAbestMove(test_state,depth)
    game.show(test_state)

print("fin")

# -*- coding: utf-8 -*-

from tkinter import *
from ai import *
import game
import minMaxAlgorithm
from sys import platform

#TODO: Change "initial_state" instances to "state" instances

boardWidth = 400
boardHeight = 400
ncols = 5
nrows = 5
cellWidth = boardWidth / ncols
cellHeight = boardHeight / nrows


COLOR = 'grey'
COLOR1 = 'sky blue'
COLOR2 = 'violet red'

BGCOLOR = '#41B77F'

depth = 2

initial_state = State([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], 4, 4, 1)



class Interface():
    def __init__(self):

        self.mode = 0

        self.window = Tk()
        self.window.title("Teeko Game")

        #print("platform = " + str(sys.platform()))
        print(sys.platform)

        self.frame = Frame(self.window)
        self.frame.config(background=BGCOLOR)

        self.title = Label(self.frame, text="Welcome to our Teeko game!", font= ("Courrier", 40), bg=BGCOLOR, fg="White")
        self.title.pack(pady= 30, fill=X)

        self.playButton = Button(self.frame, text = "Play", font= ("Courrier", 25), bg=BGCOLOR,command = lambda: [self.window.withdraw(), self.openPlayConfig()])
        self.playButton.pack(pady= 20, fill=X)

        self.howButton = Button(self.frame, text = "How to play",font= ("Courrier", 25), bg=BGCOLOR, command = lambda: [self.window.withdraw(), self.openHowTo()])
        self.howButton.pack(pady= 20, fill=X)


        self.quitButton = Button(self.frame, text = "Quit", font= ("Courrier", 25), bg=BGCOLOR, command = self.window.quit)
        self.quitButton.pack(pady= 20, fill=X)

        self.frame.pack(expand=YES)

        self.window.geometry('600x400')
        self.window.minsize(600,400)
        self.window.config(background=BGCOLOR)
        self.center_window(self.window, 600, 400)

        #Icons
        if (sys.platform == 'win32' or sys.platform == 'darwin'):
            self.window.iconbitmap('Assets/gameIcon.ico')
            self.icon = Image("photo", file="Assets/icon.png")
            self.window.call('wm','iconphoto', self.window._w, self.icon)
        elif (sys.platform == "linux"):
            self.window.iconbitmap('Assets/gameIcon.xpm')

        self.window.mainloop()


    def center_window(self, wind, w, h):
        # get screen width and height
        ws = wind.winfo_screenwidth()
        hs = wind.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        wind.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def openPlayConfig(self):
        self.playConfig = Tk()
        self.playConfig.title("Game configuration")

        frame = Frame(self.playConfig)
        frame.config(background=BGCOLOR)


        #Game config window

        difficultyLabel = Label(frame, text="Choose your difficulty level:", font =("Courrier", 15), bg=BGCOLOR, fg="White")
        difficultyLabel.pack()
        self.selector = Scale(frame, from_=0, to=200, orient=HORIZONTAL, bg=BGCOLOR, fg="White")
        self.selector.pack(expand = YES, pady= 10, fill=X)

        pvpButton = Button(frame, text="PvP", bg = BGCOLOR, command = lambda : self.changeMode(0))
        pvaiButton =  Button(frame, text="PvAI", bg = BGCOLOR, command = lambda : self.changeMode(1))

        pvpButton.pack(expand = YES, side = 'left', pady= 20, fill=X)
        pvaiButton.pack(expand = YES, side = 'left', pady= 20, fill=X)

        frame.pack(expand = YES)

        self.modeLabel = Label(self.playConfig, text="Mode selected : PvP", font=("Courrier, 20"), fg = "White",  bg = BGCOLOR)
        self.modeLabel.pack(expand=YES)

        self.playConfig.minsize(1200,400)
        self.playConfig.configure(bg=BGCOLOR)

        popupButton = Button(self.playConfig, text="Back", font=("Courrier, 20"), command = lambda: [self.playConfig.withdraw(),self.window.deiconify()], bg=BGCOLOR)
        popupButton.pack(side="bottom", pady=20)

        launchGameButton = Button(self.playConfig, text='Launch Game', font=("Courrier, 20"), command = lambda: [self.playConfig.withdraw(),self.openGameWindow()], bg=BGCOLOR )
        launchGameButton.pack(side="bottom", pady=20)
        self.center_window(self.playConfig, 1200, 300)

    def changeMode(self, i):
        #self.mode = 1 if (i == 1) else 0
        self.mode = 1 if i == 1 else 0
        modeText = "PvP" if self.mode == 0 else "PvAI"
        self.modeLabel.config(text="Mode selected : " + modeText)
        print("mode = " + str(self.mode))

    def openHowTo(self):
        howToPopup = Tk()
        howToPopup.title("How to play")


        txt1 = Label(howToPopup, text="FIRST PHASE [Placing] - Players alternate moves by dropping its 4 pawns into empty cells..", font = ("Courrier", 15), bg=BGCOLOR, fg="White")
        txt1.pack(expand=YES, pady=5)
        txt2 = Label(howToPopup, text="SECOND PHASE [Moving] - If no player achieved the winning goal, then each player moves one of its pawn into an adjacent orthogonal or diagonal empty cell.", font = ("Courrier", 15), bg=BGCOLOR, fg="White")
        txt2.pack(expand=YES, pady=5)
        txt3 = Label(howToPopup, text="	GOAL - A player wins when he makes a 4 in-a-row, or creates a square (this square can be of any size, i.e., 2x2 to 5x5).", font = ("Courrier", 15), bg=BGCOLOR, fg="White")
        txt3.pack(expand=YES, pady=5)

        howToPopup.minsize(1200,300)
        howToPopup.configure(bg=BGCOLOR)
        popupButton = Button(howToPopup, text="Ok!", font=("Courrier, 20"), command = lambda: [howToPopup.withdraw(),self.window.deiconify()], bg=BGCOLOR)
        popupButton.pack(side="bottom", pady=20)
        self.center_window(howToPopup, 1200, 300)

    def openGameWindow(self):
        self.gameWindow = Tk()
        self.gameWindow.title("Playing game...")
        self.gameWindow.minsize(800,800)

        self.gameFinished = False

        board = Frame(self.gameWindow)
        board.config(background=BGCOLOR)

        state = initial_state
        self.selectedPawnX = None
        self.selectedPawnY = None

        playerValue = 1 if state.t == 1 else 2

        self.txt = Label(self.gameWindow, text="Player " + str(playerValue) + "'s turn:", font= ("Courrier", 40), bg=BGCOLOR, fg="White")
        self.txt.pack(pady = (100,20))

        #self.coord = Label(self.gameWindow, text="Empty", font= ("Courrier", 40), bg=BGCOLOR, fg="White")
        #self.coord.pack(pady = 20)

        #lbl = Label(gameWindow, text="Player X's turn", font=(Courrier, 25))
        #lbl.pack()

        self.canvas = Canvas(board, width=boardWidth, height=boardHeight, bd=1, highlightthickness=0, relief='ridge')
        self.canvas.pack()
        board.pack(expand=YES)

        #grid = generatGrid(nrows, ncols)
        ##grid = generateBoard(initial_state)
        #drawGrid(canvas, grid)
        ##drawBoard(canvas, grid)
        self.drawBoard(self.canvas, initial_state)


        btn = Button(self.gameWindow, text="Quit game", bg=BGCOLOR, command = lambda: [self.gameWindow.withdraw(), self.window.deiconify(), initial_state.initialize()]) # TODO: Reinitialize board
        btn.pack(side="bottom", pady= 20)
        self.gameWindow.config(background=BGCOLOR)
        self.center_window(self.gameWindow,800,800)

        ###

    def onClick(self, event): #TODO: Incorporate game logic in this function
        #print("\nIt's been clicked!")
        y = int(event.x // cellWidth)
        x = int(event.y // cellHeight)
        print("x = " + str(x))
        print("y = " + str(y))
        #self.coord.config(text = "("+str(x)+","+str(y)+")")

        global initial_state

        try:
            print("selected X = " + str(self.selectedPawnX))
            print("selected Y = " + str(self.selectedPawnY))
        except:
            print("none")

        if (initial_state.board[x][y] != 0 and initial_state.a == 0 and initial_state.b == 0): #TODO: Do it with state.b too
            self.selectedPawnX = x
            self.selectedPawnY = y


        if(self.gameFinished == False):

            if (initial_state.a != 0 or initial_state.b !=0 ): #Placing phase

                    if (game.place(initial_state, x, y, True) == True):


                        if (self.mode == 0):
                            print("PvP")

                            if (initial_state.t == 1):
                                initial_state.a -= 1
                            else:
                                initial_state.b -= 1




                        elif (self.mode == 1):
                            print("PvAI")

                            #initial_state.a -= 1

                            self.txt.config(text="AI")
                            initial_state.t *= -1

                            initial_state = minMaxAlgorithm.IAbestMove(initial_state, depth)
                            initial_state.b -= 1



            else: #Moving Phase
                try:
                    if (self.selectedPawnX != None and self.selectedPawnY != None):
                        if(game.move(initial_state, self.selectedPawnX, self.selectedPawnY, x, y, True) == False):
                            print("Move failed")
                        else:
                            print("Move successful!")
                            self.selectedPawnX = None
                            self.selectedPawnY = None

                            if (self.mode == 1):
                                self.txt.config(text="AI")
                                initial_state = minMaxAlgorithm.IAbestMove(initial_state, depth)


                except:
                    print("Fail")



        self.drawBoard(self.canvas, initial_state) #Refreshes the board
        playerValue = 1 if initial_state.t == 1 else 2
        self.txt.config(text="Player " + str(playerValue) + "'s turn:")

        if (initial_state.a == 0 or initial_state.b == 0):
            if (game.isWinning(initial_state,1)):
                print("Player 1 won this game!")
                self.txt.config(text="Congrats, you've won!")
                self.gameFinished = True
            elif (game.isWinning(initial_state, -1)):
                print("Player 2 won this game!")
                self.txt.config(text="Booo, you lost :(")
                self.gameFinished = True
        print(initial_state.a)
        print(initial_state.b)



    def drawCell(self, canvas, x, y, s):
        x1 = cellWidth * x
        y1 = cellHeight * y
        x2 = x1 + cellWidth
        y2 = y1 + cellHeight

        if (s == 1):
            self.canvas.create_rectangle(x1, y1, x2, y2, fill= COLOR1, activefill= COLOR)
        elif (s == -1):
            self.canvas.create_rectangle(x1, y1, x2, y2, fill= COLOR2, activefill= COLOR)
        else:
            self.canvas.create_rectangle(x1, y1, x2, y2, fill= 'white', activefill= COLOR)
        self.canvas.bind('<Button-1>', self.onClick)



    def drawBoard(self, canvas, state):

        for i in range(5):
            for j in range(5):
                s = state.board[i][j]
                self.drawCell(self.canvas, j,i,s)
        return #



    ###

app = Interface()


###

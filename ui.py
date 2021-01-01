# -*- coding: utf-8 -*-

from tkinter import *
from ai import *
import game
import sys


#Board dimensions
boardWidth = 400
boardHeight = 400
ncols = 5
nrows = 5
cellWidth = boardWidth / ncols
cellHeight = boardHeight / nrows

#Colors used
COLOR = 'grey'
COLOR1 = 'sky blue'
COLOR2 = 'violet red'
BGCOLOR = '#41B77F'

depth = 2


state = game.boardGame([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], 1, 8)


ai = ai.TeekoAI(state,-1)



"""
@desc class of the user interface 
"""
class Interface():
    def __init__(self):

        self.mode = 0
        self.difficulty = 1



        #Main UI
        self.window = Tk()
        self.window.title("Teeko Game")

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
            #self.window.iconbitmap('Assets/gameIcon.xpm')
            pass

        self.window.mainloop()


            
    """
    @desc function that center a given window
    @param window $wind - window to be displayed at the center of the screen
    @param int $w - width of the given window
    @param int $h - height of the given window
    """ 
    def center_window(self, wind, w, h):
        # get screen width and height
        ws = wind.winfo_screenwidth()
        hs = wind.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        wind.geometry('%dx%d+%d+%d' % (w, h, x, y))

    """
    @desc function that opens the game configuration window
    """   
    def openPlayConfig(self):
        self.playConfig = Tk()
        self.playConfig.title("Game configuration")

        frame = Frame(self.playConfig)
        frame.config(background=BGCOLOR)


        #Game config window
        difficultyLabel = Label(frame, text="Choose your difficulty level:", font =("Courrier", 15), bg=BGCOLOR, fg="White")
        difficultyLabel.pack()
        self.selector = Scale(frame, from_=1, to=3, orient=HORIZONTAL, bg=BGCOLOR, fg="White")
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

        launchGameButton = Button(self.playConfig, text='Launch Game', font=("Courrier, 20"), command = lambda: [self.playConfig.withdraw(),self.openGameWindow(), self.changeDifficulty(self.selector.get())], bg=BGCOLOR )
        launchGameButton.pack(side="bottom", pady=20)
        self.center_window(self.playConfig, 1200, 300)


    """
    @desc function that changes the game mode (0 is PvP, 1 is PvAI)
    @param int $i - value the of the desired mode
    """ 
    def changeMode(self, i):
        #self.mode = 1 if (i == 1) else 0
        self.mode = 1 if i == 1 else 0
        modeText = "PvP" if self.mode == 0 else "PvAI"
        self.modeLabel.config(text="Mode selected : " + modeText)
        print("mode = " + str(self.mode))


    """
    @desc function that changes the difficulty level
    @param int $i - value the of the desired difficulty
    """ 
    def changeDifficulty(self, i):
        self.difficulty = i
        print("difficulty level " + str(self.difficulty))

    """
    @desc function that opens the "How to play" window
    """ 
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

    """
    @desc function that opens the game window
    """ 
    def openGameWindow(self):
        self.gameWindow = Tk()
        self.gameWindow.title("Playing game...")
        self.gameWindow.minsize(800,800)

        self.gameFinished = False

        board = Frame(self.gameWindow)
        board.config(background=BGCOLOR)

        #state = initial_state
        self.selectedPawnX = None
        self.selectedPawnY = None

        playerValue = 1 if state.playerPlaying == 1 else 2

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
        self.drawBoard(self.canvas, state)


        btn = Button(self.gameWindow, text="Quit game", bg=BGCOLOR, command = lambda: [self.gameWindow.withdraw(), self.window.deiconify(), state.initialize()]) # TODO: Reinitialize board
        btn.pack(side="bottom", pady= 20)
        self.gameWindow.config(background=BGCOLOR)
        self.center_window(self.gameWindow,800,800)

        ###


    """
    @desc function that is triggered whenever a player click on the game board
    @param event $event - event that triggered this function (click on canvas)
    """ 
    def onClick(self, event):
        #print("\nIt's been clicked!")
        y = int(event.x // cellWidth)
        x = int(event.y // cellHeight)
        print("x = " + str(x))
        print("y = " + str(y))
        #self.coord.config(text = "("+str(x)+","+str(y)+")")

        global state

        try:
            print("selected X = " + str(self.selectedPawnX))
            print("selected Y = " + str(self.selectedPawnY))
        except:
            print("none")

        if (state.board[x][y] != 0 and state.remainingPawns == 0):
            self.selectedPawnX = x
            self.selectedPawnY = y


        if(self.gameFinished == False):

            if (state.remainingPawns != 0): #Placing phase

                    if (state.place(x, y, True) == True):


                        if (self.mode == 0):

                            print("PvP")

                            #state.remainingPawns -= 1

                        elif (self.mode == 1):

                            print("PvAI")

                            self.txt.config(text="AI")

                            if (self.difficulty == 1):
                                ai.playEasy()
                            elif (self.difficulty == 2):
                                state = ai.playMediumOrHard(depth,0)
                            elif (self.difficulty == 3):
                                state = ai.playMediumOrHard(depth,1)
                            else:
                                print("Error\n")

            else: #Moving Phase
                try:
                    if (self.selectedPawnX != None and self.selectedPawnY != None):
                        if(state.move(self.selectedPawnX, self.selectedPawnY, x, y, True) == False):
                            print("Move failed")
                        else:
                            print("Move successful!")
                            self.selectedPawnX = None
                            self.selectedPawnY = None

                            if (self.mode == 1):
                                self.txt.config(text="AI")

                                if (self.difficulty == 1):
                                    ai.playEasy()
                                elif (self.difficulty == 2):
                                    state = ai.playMediumOrHard(depth,0)
                                elif (self.difficulty == 3):
                                    state = ai.playMediumOrHard(depth,1)
                                else:
                                    print("Error\n")

                except:
                    print("Fail")



        self.drawBoard(self.canvas, state) #Refreshes the board
        playerValue = 1 if state.playerPlaying == 1 else 2
        self.txt.config(text="Player " + str(playerValue) + "'s turn:")

        if (state.winner() != 0):
            if (state.winner() == 1):
                self.txt.config(text="Congrats, you've won!")
            else:
                self.txt.config(text="Booo, you lost :(")
            self.gameFinished = True
            

    """
    @desc function that draws an individual board cell
    @param Tk.canvas $canvas - canvas object of the tkinter library
    @param int $x - x position of the cell on the board
    @param int $y - y position of the cell on the board
    @param int $s - value the of pawn occupating this position
    """       
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


    """
    @desc function that draws the entire game board
    @param Tk.canvas $canvas - canvas object of the tkinter library
    @param gameBoard $state - game state to be drawn
    """   
    def drawBoard(self, canvas, state):

        for i in range(5):
            for j in range(5):
                s = state.board[i][j]
                self.drawCell(self.canvas, j,i,s)
        return #



    ###

app = Interface()


###

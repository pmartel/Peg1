# Peg puzzle using tkinter
# Phil Martel
# there are small differences between Python 2.7 and 3.4  Among them in that in 2.7
# it's called Tkinter

from tkinter import *

class Application(Frame):
    """ build the basic window frame template"""
    buttons = []

    def __init__(self,master,board):
        super(Application,self).__init__(master)
        self.grid()
        board.master = self # link so board can access App's graphics
        self.buttons = []
        self.create_widgets(board)

    def create_widgets(self,board):
        self.label1 = Label(self, text = '{0} Pegs left'.format(\
            int(board.pegsLeft)))
        self.label1.grid(row = 0, column=2*board.size+1, sticky = W)
        self.draw_board(board)
        #self.button1 = Button(self, text = 'Click me!', command=self.display)
        #self.button1.grid(row = 1, column=0, sticky = W)

    def display(self):
        """ event handler for the button"""
        self.background = "black"
        #self.fg = "black"
        print('The button in the window was clicked')

    def draw_board(self,board):
        """ erase the board and re-draw it """
        self.buttons.clear()
        for h in board.holes :
            
            b = Button(self, background = h.get_color(), command = self.display )
            b.grid(row = h.row, column = h.col, sticky = W)
            self.buttons.append(b)
        pass

class Board:
    master = []
    shape = ''
    size = 0
    pegsLeft=[]
    holes=[]  #list of holes
    gString = '0x0' #geometry string to pass to Tk
    boxSize = 20 #constant for size of hole

    def triangle( self ):
        """sets up or resets a trinangular board"""
        size = self.size
        self.holes.clear()
        numHoles = size*(size-1)/2
        self.pegsLeft = numHoles-1
        for r in range(size+1):
            c0 = size -r # starting column for row
            if r>0 : #state of hole
                s = 'full'
            else:
                s = 'empty'
                
            for c in range(r):
                h = Hole(row=r,col=(c0 +2*c),but=[],state=s)
                self.holes.append(h)
                print( 'row:{0} col:{1} state:{2} color:{3}'.format(\
                    h.row, h.col, h.state, h.get_color()) )
                pass
        
        self.gString = '{0}x{1}'.format(2*size*self.boxSize,\
                            2*size*self.boxSize)

    def cross(self):
        pass

    def draw(self):
        """ run through the list of holes and draw them in color"""
        #for h in self.holes
     
    def __init__( self, shape, size):
        """ set up a peg board of a given size and shape"""
        self.shape = shape
        self.size = size
        if shape == 'triangle':
            self.triangle()
        elif shape == 'cross':
            self.cross()

class Hole:
    col = [] #position of hole on grid
    row = []
    state =[] #current and initial state
    initState =[]
    but = [] #button handle
   # mapping of state into peg color also provides a list of states
    stateMap = { 'empty': 'black', 'full': 'green',
                 'target': 'brown', 'armed': 'red' }


    def __init__(self, row, col, but, state):
        self.row = row
        self.col = col
        but
        self.state = state
        self.initState = state
        self.but = but

    def reset(self):
        self.state = self.initState
        self.draw()

    # the drawing is done in the App
    def draw( self ):
        self.but.bg = self.stateMap[self.state]

    def get_color(self):
        return self.stateMap[self.state]
                  
    def setState(self, state ):
        if state in self.stateMap :
            self.draw()
        else :
            print( 'State '+state+' is not valid')
        
#main program        
# This creates a window
root = Tk()
# add a title and size
root.title('Peg Puzzle')
root.geometry('100x300')
board = Board(shape = 'triangle', size = 6)
root.geometry(board.gString)
app = Application(root,board)
#app.mainloop()
    
    

# Peg puzzle using tkinter
# Phil Martel
# there are small differences between Python 2.7 and 3.4  Among them in that in 2.7
# it's called Tkinter

from tkinter import *

# Puzzle has a board, Board has Holes, Holes have Buttons
# start moving things in that direction

class Puzzle(Frame):
    """ build the basic window frame template"""
    board = []
    buttons = []
    shape = 'triangle'
    size = 6

    def __init__(self,root):
        root.title('Peg Puzzle')
        root.geometry('100x300')
        self.board = Board(shape = self.shape, size = self.size)
        root.geometry(self.board.gString)
        super(Puzzle,self).__init__(root)
        self.grid()
        self.board.root = self # link so board can access App's graphics
        self.buttons = []
        self.create_widgets(self.board)

    def clear_board(self):
        print( 'clear the board')
        
    def create_widgets(self,board):
        self.label1 = Label(self, text = '{0} Pegs left'.format(\
            int(board.pegsLeft)))
        self.label1.grid(row = 0, column=2*board.size+1, sticky = W)
        self.draw_board(self.board)
        size = self.board.size
        self.clearButton = Button(self, text='Clear',\
                                  command = self.clear_board)
        self.clearButton.grid(row =size,column = 2*size+1)
        #self.button1 = Button(self, text = 'Click me!', command=self.display)
        #self.button1.grid(row = 1, column=0, sticky = W)

    def draw_board(self,board):
        """ erase the board and re-draw it """
        board.__init__(shape = self.shape, size = self.size)
        print( 'drawing ',self.shape,' board size ',self.size)
        pass
    

class Board:
    boxSize = 20 #constant for size of hole
    gString = '0x0' #geometry string to pass to Tk
    holes=[]  #list of holes
    pegsLeft=[]
    root = []
    shape = ''
    size = 0

    def __init__( self, shape, size):
        """ set up a peg board of a given size and shape"""
        self.shape = shape
        self.size = size
        if shape == 'triangle':
            self.triangle()
        elif shape == 'cross':
            self.cross()

    def cross(self):
        pass

    def draw(self):
        """ run through the list of holes and draw them in color"""
        #for h in self.holes
        pass

    def triangle( self ):
        """sets up or resets a trinangular board"""
        size = self.size
        self.holes.clear()
        numHoles = size*(size-1)/2
        self.pegsLeft = numHoles-1
        for r in range(size+1):
            c0 = size -r +1# starting column for row
            if r > 1 : #state of hole
                s = 'full'
            else:
                s = 'empty'
                
            for c in range(r):
                h = Hole(root,row=r,col=(c0 +2*c),but=[],state=s)
                self.holes.append(h)
##                print( 'button{4} row:{0} col:{1} state:{2} color:{3}'.format(\
##                    h.row, h.col, h.state, h.get_color(),len(self.holes)) )
                pass
        
        self.gString = '{0}x{1}'.format(4*size*self.boxSize,\
                            2*size*self.boxSize)

        
class Hole:
    but = [] #button handle
    col = [] #position of hole on grid
    row = []

    state =[] #current and initial state
    initState =[]
    
   # mapping of state into peg color also provides a list of states
    stateMap = { 'empty': 'black', 'full': 'green',
                 'target': 'brown', 'armed': 'red' }


    def __init__(self, root,row, col, but, state):
        self.row = row
        self.col = col
        #but
        self.state = state
        self.initState = state
        self.but = Button(root, bg = self.get_color(), width =2,\
                       command = self.setState )
        self.but.grid(row = row, column = col, padx=1,pady=1)

    def reset(self):
        self.state = self.initState
        self.draw()

    # the drawing is done in the App
    def draw( self ):
        self.but['bg'] = self.stateMap[self.state]
 
    def get_color(self):
        return self.stateMap[self.state]
                  
    def setState(self):
        s = self.state
        if s in self.stateMap :
            if s == 'empty':
                self.state = 'full'
            elif s == 'full':
                self.state = 'target'
            elif s == 'target':
                self.state = 'armed'
            elif s == 'armed':
                self.state = 'empty'
            self.draw()
        else :
            print( 'State '+state+' is not valid')
        
#main program        
# This creates a window
root = Tk()
# add a title and size
puzzle = Puzzle(root)
#app.mainloop()
    
    

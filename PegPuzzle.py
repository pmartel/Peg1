# Peg puzzle using tkinter
# Phil Martel
# there are small differences between Python 2.7 and 3.4  Among them in that in 2.7
# it's called Tkinter

from tkinter import *
from TwoD import *

# Puzzle has a board, Board has Holes, Holes have Buttons
# start moving things in that direction

class Puzzle(Frame):
    """ build the basic window frame template"""
    board = []
    shape = 'triangle'
    size = 6

    def __init__(self,root):
        root.title('Peg Puzzle')
        root.geometry('100x300')
        #create the board
        self.board = Board(shape = self.shape, size = self.size)
        root.geometry(self.board.gString)
        super(Puzzle,self).__init__(root)
        self.grid()
        self.board.root = self # link so board can access App's graphics
        self.create_widgets(self.board)

    def clear_board(self):
        b = self.board
        h = b.holes
        for i in range(len(h)):
            h[i].state = h[i].initState
            h[i].draw()
        b.countPegs()
        self.labelLeft['text']= '{0} Pegs left'.format(\
            int(b.pegsLeft))

        
    def create_widgets(self,board):
        """ set up label for peg count and clear button"""
        self.labelLeft = Label(self, text = '{0} Pegs left'.format(\
            int(board.pegsLeft)))
        self.labelLeft.grid(row = 0, column=2*board.size+1, sticky = W)
        self.draw_board(self.board)
        size = self.board.size
        self.clearButton = Button(self, text='Clear',\
                                  command = self.clear_board)
        self.clearButton.grid(row =size,column = 2*size+1)

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
    root = [] #  'pointer to Tk object
    adjMat = [] # adjacency matrix
    
    # copies of the parameters used to build the board
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

    def countPegs(self):
        """ counts the number of pegs left on the board """
        self.pegsLeft = 0
        h = self.holes
        for i in range(len(h)):
            h[i].state = h[i].initState
            if h[i].state == 'full':
                self.pegsLeft += 1

    def any_armed(self):
        """ determine the (first) hole that is armed (if any) """
        h = self.holes
        for i in range(len(h)):
            if h[i].state == "armed":
                return i
        return None

    def normalStates(self):
        """ get rid of armed and target states """
        for h in self.holes: # don't need index
            if h.state != "empty":
                h.state = 'full'
            h.draw()
    
    ## shapes (called from __init__())   
    def cross(self):
        """sets up or resets a cross-shaped board"""
        pass

    def triangle( self ):
        """sets up or resets a triangular board"""
        size = self.size
        self.holes.clear()
        self.holes=[]
        numHoles = size*(size-1)/2
        for r in range(size):
            c0 = size -r # starting column for row
            print( r,c0,end='|')
            if r > 0 : #state of hole
                s = 'full'
            else:
                s = 'empty'
                
            for c in range(r+1):
##                print(c, end =' ')
                h = Hole(self, root,row=r,col=c, drawCol=(c0 +2*c),but=[],state=s)
                self.holes.append(h)
##                print( 'button{4} row:{0} col:{1} state:{2} color:{3}'.format(\
##                    h.row, h.col, h.state, h.get_color(),len(self.holes)) )
                pass
##            print()
        self.gString = '{0}x{1}'.format(4*size*self.boxSize,\
                            2*size*self.boxSize)
        self.countPegs()
        
        
        # adjMat will be a 2D map with hole numbers at the corresponding
        # position
        self.adjMat = TwoD(self.size,self.size)
        h = self.holes
        for i in range(len(h)):
            r0 = h[i].row
            c0 = h[i].col
            self.adjMat.set(r0,c0,i)
##        self.adjMat.display()

        # for the triangular board adjacenct (and jumpTo) is along 3 lines:
        # 1. ne-sw.  Row +/-1, same Col
        # 2. nw-se.  Row +/- 1, Col +/-1
        # 3. e-w. Col +/- 1, same Row
            
        for j in range(len(h)):
            r = h[j].row
            c = h[j].col
            #line 1
            a1 = self.adjMat.get(r+1,c)
            if a1 != None:
                j1 = self.adjMat.get(r+2,c)
                if j1 != None:
                    h[j].addA(a1,j1)
                    
            a2 = self.adjMat.get(r-1,c)
            if a2 != None:
                j2 = self.adjMat.get(r-2,c)
                if j2 != None:
                    h[j].addA(a2,j2)
            
            #line 3
            a1 = self.adjMat.get(r,c+1)
            if a1 != None:
                j1 = self.adjMat.get(r,c+2)
                if j1 != None:
                    h[j].addA(a1,j1)
                    
            a2 = self.adjMat.get(r,c-1)
            if a2 != None:
                j2 = self.adjMat.get(r,c-2)
                if j2 != None:
                    h[j].addA(a2,j2)

            #line 2
            a1 = self.adjMat.get(r+1,c+1)
            if a1 != None:
                j1 = self.adjMat.get(r+2,c+2)
                if j1 != None:
                    h[j].addA(a1,j1)
                    
            a2 = self.adjMat.get(r-1,c-1)
            if a2 != None:
                j2 = self.adjMat.get(r-2,c-2)
                if j2 != None:
                    h[j].addA(a2,j2)

        
class Hole:
    but = [] #button handle
    #row and col are used for adjacency
    #row and drawCol are used for drawing position
    col = []
    drawCol = []
    row = []

    root = [] # points to Tk for Button
    board = [] # board associated with hole 

    # these holds adjacent holes and holes you can jump to
    adjDict = {}

    
    state =[] #current and initial state
    initState =[]
    
   # mapping of state into peg color also provides a list of states
    stateMap = { 'empty': 'black', 'full': 'green',
                 'target': 'brown', 'armed': 'red' }


    def __init__(self, board,root,row, col, drawCol, but, state):
        """ set up a hole at a given row column and state"""
        self.board = board
        self.row = row
        self.col = col
        self.drawCol = drawCol # column on Tk grid to draw hole
        self.root = root # a handle to get to the top and tkinter
        self.state = state
        self.initState = state
        self.but = Button(root, bg = self.get_color(), width =2,\
                       command = self.pressed )
        self.but.grid(row = row, column = drawCol, padx=1,pady=1)
        #initialize the adjacency dictionary
        self.adjDict={}

    def addA(self, a, j):
        self.adjDict.update({a:j})

    def reset(self):
        self.state = self.initState
        self.draw()

    def draw( self ):
        """ change the color of the hole to match its state """
        self.but['bg'] = self.stateMap[self.state]
 
    def get_color(self):
        """ get the color of a hole """
        return self.stateMap[self.state]
                  
    def set_color( self,color ):
        """set the color of a hole (for debug)"""
        self.but['bg'] = color
        
    def pressed(self):
        """ handle the button being pressed """
        print( 'pressed({0},{1}) state={2}'.format(self.row,self.col,self.state))
        if self.state == 'full':
            # Only allow one armedhole at a time
            if self.board.any_armed() == None :
                self.state = 'armed'
            else:
                # some warning?
                pass
        elif self.state == 'armed':
            self.state = 'full'
            self.board.normalStates()
        elif self.state == 'target':
            self.state = 'empty'
            self.board.normalStates()
            #decrement count
        # ignore 'empty' - do nothing
        self.draw()
        
#main program        
# This creates a window
root = Tk()
# add a title and size
puzzle = Puzzle(root)
#app.mainloop()
    
    

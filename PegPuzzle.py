# Peg puzzle using tkinter
# Phil Martel
# there are small differences between Python 2.7 and 3.4  Among them in that in 2.7
# it's called Tkinter

from tkinter import *
from TwoD import *
from Holes import Hole

# Puzzle has a board, Board has Holes, Holes have Buttons
# start moving things in that direction
# it looks like I need to get at puzzle from board so that I can set the count
# to the label of the clear button. The clear button is part of the puzzle
# frame. 

#global root

class Puzzle(Frame):
    """ build the basic window frame template"""
    board = []
    shape = 'triangle'
    size = 6
    countLabel = [] # make the countLabel "public"
    tk = [] 
    def __init__(self,tk):
        root.title('Peg Puzzle')
        root.geometry('100x300')
        self.tk = tk # pointer to Tk
        print('in Puzzle__init__(',tk,')')
        #create the board
        self.board = Board(shape = self.shape, size = self.size, parent=self)
        tk.geometry(self.board.gString)
        super(Puzzle,self).__init__(tk)
        self.grid()
        self.board.tk = self # link so board can access App's graphics
        self.create_widgets(self.board)


    def clear_board(self):
        b = self.board
        h = b.holes
        for i in range(len(h)):
            h[i].state = h[i].initState
            h[i].draw()
        b.countPegs()
        self.fixCount(b.pegsLeft)

    def fixCount(self,n):
        s = '{0} Pegs left'.format(int(n))
#        print( 'setting',s)
        self.countLabel['text']= s
        
    def create_widgets(self,board):
        """ set up label for peg count and clear button"""
        #self.draw_board(self.board)
        size = self.board.size
        self.countLabel = Label(self, text = '{0} Pegs left'.format(\
            int(board.pegsLeft)))
        self.countLabel.grid(row = 0, column=self.board.maxDrawCol,\
                             sticky = 'W')       
        #self.countLabel.grid(row = 0, column=0,sticky = 'W')       
        self.clearButton = Button(self, text='Clear',\
                                  command = self.clear_board)
        self.clearButton.grid(row =size+1,column = 0)
        self.helpButton = Button(self,text='Help')
        self.helpButton.grid(row =size+1,column = 1)
        self.overLabel = Label(self, text = '')
        self.overLabel.grid(row = size+1, column=3, sticky = W)

##    def draw_board(self,board):
##        """ erase the board and re-draw it """
##        board.__init__(shape = self.shape, size = self.size,\
##                       parent =self)

    def gameOver(self, flag):
        if not(flag):
            self.overLabel['text']='Game Over'
        else:
            self.overLabel['text']='g'
        pass
    
class Board:
    boxSize = 20 #constant for size of hole
    gString = '0x0' #geometry string to pass to Tk
    holes=[]  #list of holes
    pegsLeft=[]
    #tk = [] #  'pointer to Tk object
    adjMat = [] # adjacency matrix
    parent = [] 
    # copies of the parameters used to build the board
    shape = ''
    size = 0
    maxDrawCol = 0

    def __init__( self, shape, size, parent):
        """ set up a peg board of a given size and shape"""
        self.parent = parent
        self.shape = shape
        self.size = size
        print( 'drawing ',self.shape,' board size ',self.size)
        if shape == 'triangle':
            self.triangle()
        elif shape == 'cross':
            self.cross()

    def countPegs(self):
        """ counts the number of pegs left on the board """
        self.pegsLeft = 0
        h = self.holes
        for i in range(len(h)):
            if h[i].state == 'full':
                self.pegsLeft += 1
        
    def any_armed(self):
        """ determine the (first) hole that is armed (if any) """
        h = self.holes
        for i in range(len(h)):
            if h[i].state == "armed":
                return i
        return None

    def anyTargets(self):
        """ detrmine if there are any targets remaining on the board"""
        for h in self.holes:
            if h.checkTargets():
                return True
        return False
    
    def dumpHoles(self):
        """ print list of hole properties """
        print('hole\tstate')
        for x in self.holes:
            print(x.index, x.state)

	
    def normalStates(self):
        """ get rid of armed and target states """
        for h in self.holes: # don't need index
            s = h.state
            if s == "armed":
                h.state = 'full'
            elif s == "target":
                h.state = "empty"
            h.draw()
        self.countPegs()
        self.parent.fixCount(self.pegsLeft)
    
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
            c0 = size -r -1# starting column for row
            if r > 0 : #state of hole
                s = 'full'
            else:
                s = 'empty'
                
            for c in range(r+1):
                drawCol=(c0 +2*c)
                h = Hole(self, self.parent.tk, row=r,col=c, drawCol=drawCol,\
                         but=[], state=s,index = len(self.holes))
                self.holes.append(h)
                self.maxDrawCol = max(self.maxDrawCol,drawCol)
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
           
## Holes class split off into a separate file

        
#main program        
# This creates a window
root = Tk()

# start the puzzle
puzzle = Puzzle(root)
#app.mainloop()
# for debug
b = puzzle.board
h=b.holes
print('graphics info')
print('root',root)
print('index','hole',sep='\t')
for i in range(len(h)):
    print(i,str(h[i].but),sep='\t')

print('countLabel',puzzle.countLabel)
print('overLabel',puzzle.overLabel)
print('clearButton',puzzle.clearButton)
print('helpButton',puzzle.helpButton)

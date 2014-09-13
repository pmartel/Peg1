# the Hole class is now in thes file instead of puzzle.py

from tkinter import *

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
    # if I'm a target, this is who is targeting me and who's being jumped
    # these wre originally set by h[v].targeter = self, but this puts a copy
    # of self into targeter, rather than a "pointer" to the original self
    # using index should get around this
    targeter = []
    jumped =[]
    
    state =[] #current and initial state
    initState =[]

    index = [] # positin of this hole in board.holes
    
   # mapping of state into peg color also provides a list of states
    stateMap = { 'empty': 'black', 'full': 'green',
                 'target': 'brown', 'armed': 'red' }


    def __init__(self, board,root,row, col, drawCol, but, state,index):
        """ set up a hole at a given row column and state"""
        self.board = board
        self.row = row
        self.col = col
        self.drawCol = drawCol # column on Tk grid to draw hole
        self.root = root # a handle to get to the top and tkinter
        self.state = state
        self.initState = state
        self.index = index
        self.but = Button(root, bg = self.get_color(), width =2,\
                       command = self.pressed )
        self.but.grid(row = row, column = drawCol, padx=1,pady=1)
        #initialize the adjacency dictionary
        self.adjDict={}
        self.targeter = {}

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

    def checkTargets(self):
        """ check if this cell has any targets """
        h =self.board.holes
        if self.state == 'full':
            for k in self.adjDict.keys():
                v = self.adjDict[k]
                if h[k].state == 'full' and h[v].state == "empty" :
                    return True
        return False
                  
    def getTargets(self):
        """Called when the button is pressed.  creates a dictionary with real
        targets as the keys and adjacent points as the values returns True if at
        least 1 target"""
    
        h =self.board.holes
        retVal = False
        for k in self.adjDict.keys():
            v = self.adjDict[k]
            if h[k].state == 'full' and h[v].state == "empty" :
                h[v].targeter = self.index
                h[v].jumped = h[k].index
                h[v].state = "target"
                h[v].draw()
                retVal = True
            else:
                h[v].targeter = [] # just in case
        return retVal
    
    def set_color( self,color ):
        """set the color of a hole (for debug)"""
        self.but['bg'] = color
        
    def pressed(self):
        """ handle the button being pressed """
#        print( 'pressed({0},{1}) state={2}'.format(self.row,self.col,self.state))
        if self.state == 'full':
            # Only allow one armed hole at a time
            if self.board.any_armed() == None :
                # a hole should only be armed if there is at least one empty target
                targets = self.getTargets()
                if targets:
                    self.state = 'armed'
            else:
                # some warning?
                pass
        elif self.state == 'armed':
            self.state = 'full'
            self.board.normalStates()
        elif self.state == 'target':
            # this is an interesting one.  A jump occurs, the target becomes empty
            # as does the hole adjacent hole. This hole becomes full
            h = self.board.holes
            h[self.index].state = 'full' # trying this...
            h[self.targeter].state = 'empty'
            h[self.jumped].state = 'empty'
            self.board.normalStates()
            self.board.parent.gameOver(self.board.anyTargets())

        # ignore 'empty' - do nothing
        self.draw()


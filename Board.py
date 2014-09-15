# the Board class is now a separate file
from Holes import Hole
from TwoD import *

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

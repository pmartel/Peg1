# Peg puzzle using tkinter
# Phil Martel
# there are small differences between Python 2.7 and 3.4  Among them in that in 2.7
# it's called Tkinter

from tkinter import *
from Board import Board

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
        self.gameOver(False)

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
    
## Board class split off into separate file           
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

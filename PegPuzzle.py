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

# it looks like I might have to make the labels and buttons part of the board
# rather than the puzzle.

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
        #create the board
        self.board = Board(shape = self.shape, size = self.size, parent=self)
        tk.geometry(self.board.gString)
        super(Puzzle,self).__init__(tk)
        self.grid()
        self.board.tk = self # link so board can access App's graphics
    
## Board class split off into separate file which now has the
##buttons and labels          
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
##print('graphics info') print('root',root)
##print('index','hole',sep='\t') for i in range(len(h)):
##print(i,str(h[i].but),sep='\t')
##
##print('countLabel',b.countLabel)
##print('overLabel',b.overLabel)
##print('clearButton',b.clearButton)
##print('helpButton',b.helpButton)

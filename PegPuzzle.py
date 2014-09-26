# Peg puzzle using tkinter
# Phil Martel
# there are small differences between Python 2.7 and 3.4  Among them in that in 2.7
# it's called Tkinter

from tkinter import *
from tkMessageBox import *
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
        self.selectBoard()
        #create the board
        self.board = Board(shape = self.shape, size = self.size, parent=self)
        tk.geometry(self.board.gString)
        super(Puzzle,self).__init__(tk)
        self.grid()
        self.board.tk = self # link so board can access App's graphics
        
    def selectBoard(self):
        # it looks like a messagebox isn't what I want.  Maybe tk.Dialog()
        selectWin = self.tk.tkMessageBox();
##        selectWin.title('Select Board')
##        selectWin.geometry('300x300+600+200')
        selectWin.askokcancel(title='enter board parameters')
        l1 = Label(selectWin,text='Size')
        l1.grid(row=0,column=0)
        l3 = Label(selectWin,text='Shape')
        l3.grid(row=1,column=0)
##        sizeVar = selectWin.StringVar()
##        Ent1 = Entry(textVariable=sizeVar)
        Ent1 = Entry(selectWin)
        Ent1.grid(row=0,column=1)
        mB1=Menu(selectWin)
        #mB1.grid(row=1,column=1)
        # wait for window to close
        #selectWin.mainloop()

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

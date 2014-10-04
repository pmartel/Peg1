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
    selectBoard = []
    def __init__(self,tk):
        tk.title('Peg Puzzle')
        tk.geometry('100x300')
        self.tk = tk # pointer to Tk
        tk1 = Tk()
        self.selectBoard = SelectBoard(tk1)
        [self.shape,self.size] = self.selectBoard.waitForClose()
        
        #[self.shape, self.size] = self.selectBoard()
        #create the board
        self.board = Board(shape = self.shape, size = self.size, parent=self)
        tk.geometry(self.board.gString)
        super(Puzzle,self).__init__(tk)
        
        self.grid()
        self.board.tk = self # link so board can access App's graphics

class SelectBoard(Frame) :
    tk1 = []
    def __init__(self,tk1):
        # it looks like a messagebox isn't what I want.  Maybe tk.Dialog()
        self.tk1 = tk1
        tk1.title('Select Board')
        tk1.geometry('300x200+500+200')
        l1 = Label(tk1,text='Size')
        l1.grid(row=0,column=0)
        l3 = Label(tk1,text='Shape')
        l3.grid(row=1,column=0,sticky=N)
##        sizeVar = selectWin.StringVar()
##        Ent1 = Entry(textVariable=sizeVar)
        Ent1 = Entry(tk1)
        Ent1.grid(row=0,column=1)
        lb1=Listbox(tk1,height=4)
        lb1.insert(END,'triangle')
        lb1.insert(END,'cross')
        lb1.grid(row=1,column=1)
        b1 = Button(tk1, text='Done', command = self.validate)
        b1.grid(row=2,column=2)
        super(SelectBoard,self).__init__(tk1)
        self.grid()

    def validate(self):
        """ verify that size is a number and shape is ok """
        #debug
        pass

    def waitForClose(self):
        input('type something')
        return ['triangle', 5]
    
## Board class split off into separate file which now has the
##buttons and labels          
## Holes class split off into a separate file

        
#main program        
# This creates a window
root = Tk()

# start the puzzle
puzzle = Puzzle(root)
puzzle.mainloop()
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

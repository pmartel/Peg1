# Peg puzzle using tkinter
# Phil Martel
# there are small differences between Python 2.7 and 3.4  Among them in that in 2.7
# it's called Tkinter

from tkinter import *
from Board import Board
from winsound import *

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
        self.selectBoard = SelectBoard(self)

    def clearBoard(self):
        c = self.tk.children
        l = list(c.values())
        for k in range(len(l)):
            l[k].destroy()
      
        #[self.shape, self.size] = self.selectBoard()
##        #create the board
##        self.board = Board(shape = self.shape, size = self.size, parent=self)
##        tk.geometry(self.board.gString)
##        super(Puzzle,self).__init__(tk)
##        
##        self.grid()
##        self.board.tk = self # link so board can access App's graphics

class SelectBoard(Frame) :
    def __init__(self,puz):
        self.puz = puz
        puz.tk.title('Select Board')
        puz.tk.geometry('300x200+500+200')
        l1 = Label(puz.tk,text='Size')
        l1.grid(row=0,column=0)
        l3 = Label(puz.tk,text='Shape')
        l3.grid(row=1,column=0,sticky=N)
        self.sizeVar = StringVar()
        self.Ent1 = Entry(puz.tk,textvariable=self.sizeVar)
        self.Ent1.grid(row=0,column=1)
        self.listVar=StringVar()
        self.lb1=Listbox(puz.tk,height=4,selectmode=SINGLE,
                         listvariable=self.listVar)
        self.lb1.insert(END,'triangle')
        self.lb1.insert(END,'cross')
        self.lb1.grid(row=1,column=1)
        self.b1 = Button(puz.tk, text='Done', command = self.validate)
        self.b1.grid(row=2,column=2)
        super(SelectBoard,self).__init__(puz.tk)
        self.grid()


        
    def validate(self):
        """ verify that size is a number and shape is ok """
        #debug
        errNum = 0
        s = self.lb1.curselection()
        lstr = self.listVar.get() # string of listVar
        try:
            l = eval(lstr) # evaluates as a tuple
            bt = l[s[0]] # selects one item from tuple. Exception if s is empty
            print('board type',bt)
            self.puz.shape = bt
        except:
           print( 'no board type selected')
           MessageBeep(MB_ICONHAND) # "bad" sound in module winsound
           errNum += 1
           
        try :
            s =self.sizeVar.get()
            n = int(s)
            print('board size',n)
            self.puz.size = n
        except :
           print( 'bad board size, must be integer')
           MessageBeep(MB_ICONHAND) # "bad" sound in module winsound
           errNum += 2
            
        if errNum == 0: # good parameters, run game
           p = self.puz
           p.clearBoard()
           p.board = Board(shape = p.shape, size = p.size, parent=p)
           p.tk.geometry(p.board.gString)

## Board class split off into separate file which now has the
##buttons and labels          
## Holes class split off into a separate file

        
#main program        
# This creates a window
root = Tk()

# start the puzzle
puzzle = Puzzle(root)
#puzzle.mainloop()
# for debug
#b = puzzle.board
##h=b.holes
t = puzzle.tk
c = t.children

##print('graphics info') print('root',root)
##print('index','hole',sep='\t') for i in range(len(h)):
##print(i,str(h[i].but),sep='\t')
##
##print('countLabel',b.countLabel)
##print('overLabel',b.overLabel)
##print('clearButton',b.clearButton)
##print('helpButton',b.helpButton)

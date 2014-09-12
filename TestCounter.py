# this is the counter that goes with test.py

from tkinter import *
class Counter():
    """ Counter should generate the buttons associated with it and
    pass the count to the label defined in App"""

    count = 0
    
    def __init__(self, parent):
        self.parent = parent
        tkRoot = parent.tkRoot
        self.b1 = Button(tkRoot,command=self.inc,text='inc')
        self.b1.grid(row=1,column=0)
        self.b2 = Button(tkRoot,command=self.clear,text='clear')
        self.b2.grid(row=1,column=2)

    def inc(self):
        self.count +=1
        self.disp()

    def clear(self):
        self.count = 0
        self.disp()

    def disp(self):
        print( self.count)
        self.parent.lab1['text'] = 'count={0}'.format(self.count)

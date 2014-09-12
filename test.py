# testing
# GUI using Tkinter
from tkinter import *
from TestCounter import Counter

class App(Frame):
    """build the basic window frame template"""
    count = 0
    tkRoot = []
    #background colors to cycle through
    ground = 'red','yellow','green','blue','white','black','brown'
    
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.create_widgets()
        self.tkRoot = master
        self.counter = Counter(self)
        
    def create_widgets(self):
        """ a label that can be written to, and two buttons """
        self.lab1 = Label(self, text ='count={0}'.format(self.count))
        self.lab1.grid(row=0,column=0)


##    def disp(self):
##        self.lab1['text'] = 'count={0}'.format(self.count)
   
## main routine        
root = Tk()
root.title( 'Test window')
root.geometry('300x100')
app = App(root)
#app.mainloop()
# with the main loop commented, you can look at app
print(app.__dict__ )#dumps info about app

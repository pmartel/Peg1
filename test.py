# testing
# GUI using Tkinter
from tkinter import *

class App(Frame):
    """build the basic window frame template"""
    count = 0
    #background colors to cycle through
    ground = 'red','yellow','green','blue','white','black','brown'
    
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """ a label that can be written to, and two buttons """
        self.lab1 = Label(self, text ='count={0}'.format(self.count))
        self.lab1.grid(row=0,column=0)
        self.b1 = Button(self,command=self.inc,text='inc')
        self.b1.grid(row=1,column=0)
        self.b2 = Button(self,command=self.clear,text='clear')
        self.b2.grid(row=1,column=2)

    def inc(self):
        self.count +=1
        self.disp()

    def clear(self):
        self.count = 0
        self.disp()

    def disp(self):
        self.lab1['text'] = 'count={0}'.format(self.count)
   
## main routine        
root = Tk()
root.title( 'Test window')
root.geometry('300x100')
app = App(root)
#app.mainloop()
# with the main loop commented, you can look at app
print(app.__dict__ )#dumps info about app

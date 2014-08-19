# testing
# GUI using Tkinter
from tkinter import *

class App(Frame):
    """build the basic window frame template"""
    but =[]
    #bavckground colors to cycle through
    ground = 'red','yellow','green','blue','white','black','brown'
    
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.but.append( LocalBut(self, color='green',i = len(self.but)))
        self.but[0].b.grid(row=1,column=2,pady=2)
        self.but.append( LocalBut(self, color='brown',i = len(self.but)))
        self.but[1].b.grid(row=2,column=1,padx=3,pady=2)
        
    def pressed(self):
        #print( 'button pressed')
        # this works, try to determine which button see p165 of tkinter.pdf
        for b in self.but :
            print(b)
            print(self)
            print()
            pass 
        pass

class LocalBut():
    b = []
    i = []
    def __init__(self, master, color, i):
        self.b = Button(master, bg = color,width=2,command= self.push,\
                        overrelief=RAISED)
        #self.but.append( Button(self, col='brown',i = len(self.but)))
        self.i = i
        print( 'button ',self.i,' color ', self.b['bg'], ' command ',\
               self.b['command'])
        
    def push(self):
        print( 'button pressed', self)
        # this works, try to determine which button see p165 of tkinter.pdf
        print(self.b)
        print(self.i)
        print(self)
        print()
        bg = self.b['bg']
        if bg == 'green':
            self.b['bg'] = 'red'
        
        pass
    
    
        
root = Tk()

root.title( 'Test window')
root.geometry('300x100')
app = App(root)
#app.mainloop()
# with the main loop commented, you can look at app
print(app.__dict__ )#dumps info about app

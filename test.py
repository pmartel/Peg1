# testing
# GUI using Tkinter
from tkinter import *

class App(Frame):
    """build the basic window frame template"""
    but =[]
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.but.append( Button(self, bg='green',command = self.pressed))
        self.but[0].grid(row=1,column=2,pady=2)
        self.but.append( Button(self, bg='brown',command = self.pressed))
        self.but[1].grid(row=2,column=1,padx=3,pady=2)
        
    def pressed(self):
        #print( 'button pressed')
        # this works, try to determine which button see p165 of tkinter.pdf
        for b in self.but :
            print(b)
            print(self)
            print()
            pass 
        pass
        
root = Tk()

root.title( 'Test window')
root.geometry('300x100')
app = App(root)
#app.mainloop()
# with the main loop commented, you can loop at app
# app.__dict__ dumps info about app

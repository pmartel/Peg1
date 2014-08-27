# developing code for working with a 2-D array
class TwoD:
##    arr = []
##    cols =0
##    rows=0

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.arr = []
        rObj =[]
        for r in range(rows):
            rObj.append([])
        for c in range(cols):
            self.arr.append(rObj)

    def display(self):
        """ print the 2D array with row and column stuff on the outside"""
        t = '\t|' # marker
        print('____',end='')
        for c in range(self.cols): # column stuff
            print( t,c, end='')
        print()
        for r in range(self.rows):
            print(r, end='') # row stuff
            for c in range(self.cols):
                v = self.arr[c][r]
                print( t,v, end='')
            print()

    def seqFill(self):
        n = 0
        for r in range(self.rows):
            for c in range(self.cols):
                self.arr[c][r] = n
                n +=1

    
if __name__ == '__main__':
    a = TwoD(4,3)
    b = TwoD(3,5)
    a.seqFill()
    a.display()

    

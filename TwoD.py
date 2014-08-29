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
            # just having append(rObj) points to one copy
            self.arr.append(rObj.copy())

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

    def get(self, row, col ):
        """ get a value.  return None if outside of range """
        if row < 0 or row >= self.rows :
            return None
        if col < 0 or col >= self.cols :
            return None
        ret = self.arr[col][row]
        if ret == []:  # for the peg puzzle, a [] is out of bounds, so None
            return None
        else:
            return ret
        
    def seqFill(self):
        """ debug code """
        n = 0
        for r in range(self.rows):
            for c in range(self.cols):
                self.arr[c][r] = n
                n +=1

    def set(self, row, col, val ):
        """ get a value.  return None if outside of range """
        if row < 0 or row >= self.rows :
            return False
        if col < 0 or col >= self.cols :
            return False
        self.arr[col][row] = val
        return True

# this runs if TwoD.py is run stand-alone.
# it serves as debug code
if __name__ == '__main__':
    a = TwoD(4,3)
    b = TwoD(3,5)
    a.seqFill()
    a.display()
    print()
    print(a.get(1,2))
    print(a.get(-1,2))
    print(a.get(2,3))
    print(a.set(2,2,-1))
    print()
    a.display()
        

    

## Phil's utility library
global c1
class Hierarchy():
    """ this class is set up to help maintain a hierarchy of parent classes
up to the main application """

    def __init__( self, parent ):
        """If the class that calls this is gcreated in another class,
pass that parent class in, otherwise None """
        self.parent = parent

    def level(self):
        """ returns the hierarchy level """
        count = 0
        p = self.parent
        while p != None:
            p = p.hierarchy.parent
            count +=1
        return count

    def getRoot(self):
        """ returns the top level of the hierarchy """
        root = self
        p = root.parent
        
        while p != None:
            root = p
            p = root.hierarchy.parent
        return root

# debugging code for Hierarchy
if __name__ != 'main':
    class C1():
        def __init__(self):
            self.hierarchy = Hierarchy(None)
            self.c2 = C2(self)

    class C2():
        def __init__(self,parent):
            self.hierarchy = Hierarchy(parent)
            if self.hierarchy.level() < 5:
                self.c2 = C2(self)

        def test(self):
            print(c1)

    #main routine

    c1 = C1()

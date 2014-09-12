## Phil's utility library

class Hierarchy():
    """ this class is set up to help maintain a hierarchy of parent classes
up to the main application """

    def __init__( self, parent ):
        """If the class that calls this is gcreated in another class,
pass that parent class in, otherwise None """
        self.parent = parent

    def level(self):
       count = 0
       return count

class C1():
    def __init__(self):
        hierarchy = Hierarchy(None)
        c = C2(self)


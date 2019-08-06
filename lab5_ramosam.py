class Triangle:
    ''' Represents a triangle.

    attributes:  side1, side2, side3
    '''
    def __init__(self, side1 = 3, side2 = 4, side3 = 5):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getA(self):
        ''' Getter for side1.   '''
        return self.side1

    def setA(self, new_side_value):
        ''' Setter for side1.   '''
        self.side1 = int(new_side_value)

    def getB(self):
        ''' Getter for side2.   '''
        return self.side2

    def setB(self, new_side_value):
        ''' Setter for side2.   '''
        self.side2 = int(new_side_value)

    def getC(self):
        ''' Getter for side3.   '''
        return self.side3

    def setC(self, new_side_value):
        ''' Setter for side3.   '''
        self.side3 = int(new_side_value)

    def isEquilateral(self):
        ''' Returns True if all three sides are equal.  '''
        return self.side1 == self.side2 and self.side1 == self.side3

    def isIsosceles(self):
        ''' Returns True if at least 2 sides are the same. (2 or 3 equal sides returns True.)   '''
        return self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3

    def isScalene(self):
        ''' Returns True if no two sides are equal. '''
        return self.side1 != self.side2 and self.side1 != self.side3 and  self.side2 != self.side3

    def isRight(self):
        ''' Checks if the value of any of the three sides squared is equal to the sum of the squares of the
        other two sides, then returns True.   '''
        biggest = 0
        small1 = 0
        small2 = 0

        if self.side1 > self.side2 and self.side1 > self.side3:
            biggest = self.side1
            small1 = self.side2
            small2 = self.side3
        elif self.side2 > self.side1 and self.side2 > self.side3:
            biggest = self.side2
            small1 = self.side1
            small2 = self.side3
        elif self.side3 > self.side1 and self.side3 > self.side2:
            biggest = self.side3
            small1 = self.side1
            small2 = self.side2
        else:
            return False

        return biggest**2 == (small1**2 + small2**2)
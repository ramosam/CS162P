'''
Collection of files used to complete lab 8.
    Car.py
    CarList.py

Requirements:

    Car	Class Requirements
    Your car class should have the following:
    initializer that takes a make, color, and year (default: black 1910 Ford)
    setters and getters for all three variables
    Overloaded equality operator that matches all three variables, return true if they match, false
    otherwise
    Overloaded str() method that returns the contents as (color year make)

    List Class Requirements
    Your list class should have the following:
    a link class that contains a pointer to next and a reference to a car object
    addCar – input is make, color, year. Creates a new car, creates a new link that points to that car
    and adds it to the head of the list
    findCar – input is make, color, year. Creates a temporary car with those inputs. Uses the
    overloaded equality operator to check the list to see if such a car exists. Returns true if found, false
    otherwise
    removeHead – if list is empty, returns none. Otherwise returns the car at the head of the list
    and removes it from the list
    Overloaded str() method that uses the car str() method to create a string of all the cars in the
    list. The cars should be listed one per line.
    Overloaded len() method that returns the number of cars in the list

'''

class Car:
    def __init__(self, make = 'Ford', color = 'Black', year = 1910):
        ''' Creates a car with the provided make, color, year.
            Defaults to Ford black 1910.
        '''
        self.make = make
        self.color = color
        self.year = year
        

    # Property setters and getters
    def setMake(self, newMake):
        ''' Setter for make.    '''
        self.make = newMake

    def getMake(self):
        ''' Getter for make.    '''
        return self.make

    def setColor(self, newColor):
        ''' Setter for color.   '''
        self.color = newColor

    def getColor(self):
        ''' Getter for color.   '''
        return self.color

    def setYear(self, newYear):
        ''' Setter for year.    '''
        self.year = newYear

    def getYear(self):
        ''' Getter for year.    '''
        return self.year


    # Overloading equality operator
    def __eq__(self, otherCar):
        ''' Overloaded equality operator.  Returns True if
            color, year and make match.
        '''
        return (self.make == otherCar.make and self.color == otherCar.color and self.year == otherCar.year)

    def __str__(self):
        ''' Returns friendly string of color, year and make of Car. 
        '''
        return ("%s %s %s" % (self.color, self.year, self.make))




####################################

class Link:
    ''' Class to hold the value of an object (Car), and a variable to hold the next node in the linked list.    '''
    def __init__(self, make, color, year):
        ''' Creates an empty car link. '''
        self.car = Car(make, color, year)
        self.next = None


class CarList:
    ''' Wrapper to handle Car links. Creates empty head link.   '''
    def __init__(self):
        self.head = None

    def __len__(self):
        current = self.head
        total = 0
        while current:
            total += 1
            current = current.next
        return total

    def addCar(self, make, color, year):
        ''' Adds a car to the head of the list. '''
        tempCar = Link(make, color, year)
        tempCar.next = self.head
        self.head = tempCar

    def findCar(self, make, color, year):
        ''' Creates a temporary car and searches the list to see if it is present. Returns True if found.   '''
        current = self.head
        carInQuestion = Car(make, color, year)
        while current:
            if current.car == carInQuestion:
                return True
            current = current.next
        return False

    def removeHead(self):
        ''' Removes CarList head and returns the object found.  '''
        if self.head:
            headCar = self.head.car
            self.head = self.head.next
            return headCar
        else:
            return None

    def __str__(self):
        ''' Friendly string displaying cars in list. '''
        if self.head == None: return 'No items in list.'
        current = self.head
        curList = []
        while current:
            curList.append(str(current.car))
            current = current.next
        return '\n'.join(curList)

        


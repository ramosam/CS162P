'''Person Class
You will not actually instanBate objects of type person. This class is only used to define the common aspects of the “Instructor” and “Student” classes.
Class Variables
    firstName, lastName, age, lNumber
Class Methods 
    init– four arguments: First Name, Last Name, Age, LNumber 
    default values are empty strings and a zero for age  
    Setters – one for each variable.
    Getters – one for each variable.
    GetJob – returns “Undefined”. 
        Note, this does not access a variable, it simply returns a hard coded string.
'''

class Person:
    ''' Base class to create framework for Instructor and Student classes.  
        firstName, lastName, lNumber defaults are empty strings.
        age default is set to 0.
    '''
    def __init__(self, firstName = '', lastName = '', age = 0, lNumber = ''):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.lNumber = lNumber

    def setFirstName(self, newFirstName):
        ''' Setter for firstName.   '''
        self.firstName = newFirstName

    def getFirstName(self):
        ''' Getter for firstName.   '''
        return str(self.firstName)

    def setLastName(self, newLastName):
        ''' Setter for lastName.    '''
        self.lastName = newLastName

    def getLastName(self):
        ''' Getter for lastName.    '''
        return self.lastName

    def setAge(self, newAge):
        ''' Setter for age. '''
        self.age = newAge

    def getAge(self):
        ''' Getter for age. '''
        return self.age

    def setLNumber(self, newLNumber):
        ''' Setter for LNumber. '''
        self.lNumber = newLNumber

    def getLNumber(self):
        ''' Getter for LNumber. '''
        return self.lNumber

    def getJob(self):
        return "Undefined"


#################################################
'''
    Instructor Class
    Inherits from Person.
   
    Instructor has an addiBonal class variable – OfficeHours. You will need methods to get and set it   
    GetJob – returns “Instructor”. Again, this is not returning the value of a variable, it is simply returning a hard coded string.
'''

class Instructor(Person):
    ''' Class defining the Instructor object. Inherits from Person and implements
        additional property of Office Hours.
    '''
    def __init__(self, firstName, lastName, age, lNumber, officeHours = ''):
        ''' Initializer for Instructor, adding office hours property.   '''
        super().__init__(firstName, lastName, age, lNumber)
        self.officeHours = officeHours
        

    def setOfficeHours(self, newHours):
        ''' Setter for office hours.    '''
        self.officeHours = newHours

    def getOfficeHours(self):
        ''' Getter for office hours.    '''
        return self.officeHours

    def getJob(self):
        return "Instructor"


#################################################
''' Student Class
    Inherits from Person
    Student has an addiBonal class variable – GPA. You will need methods to get and set it.   
    GetJob – returns “Student”. As above, this is retuning a hard coded string.
'''

class Student(Person):
    ''' Class defining the Student object. Inherits from Person and implements 
        additional property of GPA.
    '''
    def __init__(self, firstName, lastName, age, lNumber, gpa = 0.0):
        ''' Initializer for Student, adding gpa property.   '''
        super().__init__(firstName, lastName, age, lNumber)
        self.gpa = gpa

    def setGPA(self, newGPA):
        ''' Setter for gpa. '''
        self.gpa = newGPA

    def getGPA(self):
        ''' Getter for student's GPA.   '''
        return self.gpa

    def getJob(self):
        return "Student"

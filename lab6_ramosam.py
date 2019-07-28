import math

class Person:
    ''' Creates a person object.

    attributes: first_name, last_name, address
    '''
    def __init__(self, first_name = "", last_name = "", address = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def getFirstName(self):
        ''' Getter for first_name.  '''
        return self.first_name

    def setFirstName(self, newFirst):
        ''' Setter for first_name.  '''
        self.first_name = newFirst

    def getLastName(self):
        ''' Getter for last_name.   '''
        return self.last_name

    def setLastName(self, newLast):
        ''' Setter for last_name.   '''
        self.last_name = newLast

    def getAddress(self):
        ''' Getter for address. '''
        return self.address

    def setAddress(self, newAddress):
        ''' Setter for address. '''
        self.address = newAddress





class CreditCard:
    def __init__(self, firstName = '', lastName = '', address = '', card_number = 0, credit_limit = 0, balance = 0, ):
        self.account_owner = Person(firstName, lastName, address)
        self.card_number = card_number
        self.balance = balance
        self.credit_limit = credit_limit

    def getOwnerName(self):
        return self.account_owner.getFirstName() + ' ' + self.account_owner.getLastName()

    def getBalance(self):
        return self.balance

    def getCardNumber(self):
        return self.card_number

    def getAddress(self):
        return self.account_owner.getAddress()

    def payBalance(self, incoming_payment):
        if incoming_payment < 0:
            # Will not process, incoming payment cannot be negative.
            return False
        else:
            # Payment of 0 or more is applied to the balance.
            self.balance -= incoming_payment
            return True

    def makeCharge(self, charge_amount):
        if charge_amount < 0:
            # If charging a negative amount then transaction will not process, 
            # charge will not be applied to balance.
            print('You cannot make a negative charge amount.')
            return False
        elif abs(charge_amount + self.balance) > self.credit_limit:
            # If the current balance and new charge amount exceed the credit limit, 
            # the transaction will be denied.
            print('You cannot make a purchase that will cause you to exceed your credit limit.')
            return False
        else:
            # Charge of 0 or more is applied to the balance.
            self.balance += charge_amount
            return True

    def getCreditLimit(self):
        return self.credit_limit

    def setCreditLimit(self, max_limit):
        if max_limit < 0:
            print('The credit limit cannot be set to a negative value.')
        else:
            self.credit_limit = max_limit


print("**********************")
print("Testing Person class:")
print("Creating default person.")
p = Person()
print("Testing getters.")
print(p)
print(p.getFirst_Name())
print(p.getLast_Name())
print(p.getAddress())
print()
print("Creating person: A, B, 123 C")
print("Testing getters.")
p1 = Person('A', 'B', '123 C')
print(p1)
print(p1.getFirst_Name())
print(p1.getLast_Name())
print(p1.getAddress())
print()
print("Default Person, p1, testing setters")
# p1.first_name = 'X'
# p1.last_name = 'Y'
# p1.address = '890 Z'
print('Before change:')
print(p1)
p1.setFirst_Name('X')
p1.setLast_Name('Y')
p1.setAddress('890 Z')
print('Updated person object.')
print(p1)
print(p1.getFirst_Name())
print(p1.getLast_Name())
print(p1.getAddress())
print()
print("**********************")
print("Testing CreditCard class:")
print("Creating default credit card.")
cc = CreditCard()
print(cc)
print(cc.account_owner.first_name)
print(cc.account_owner.last_name)
print(cc.account_owner.address)
print(cc.card_number)
print(cc.balance)
print(cc.credit_limit)
print()
print('Testing CreditCard with Person p1 in constructor.')
cc1 = CreditCard(p1)
print(cc1)
print(cc1.account_owner.first_name)
print(cc1.account_owner.last_name)
print(cc1.account_owner.address)
print(cc1.card_number)
print(cc1.balance)
print(cc1.credit_limit)
print()

print('Creating Person p: A B 123 C')
p = Person('A', 'B', '123 C')
print('Creating default card with default Person object.')
cc = CreditCard()
print('Printing cc object: ', cc)
print('cc account owner name: ', cc.getOwner_Name())
print('cc account owner address: ', cc.getAddress())
print('cc card number: ', cc.getCardNumber())
print('cc current balance: ', cc.getBalance())
print('cc credit limit: ', cc.getCreditLimit())
cc.setCreditLimit(234)
print('cc setting new credit limit - 234: ', cc.getCreditLimit())
print('cc makeCharge: 100')
cc.makeCharge(100)
print('cc current balance: ', cc.getBalance())
print('cc payBalance: 50')
cc.payBalance(50)
print('cc current balance: ', cc.getBalance())
print()

print('Creating default credit card, cc1, with Person p:')
cc1 = CreditCard(p)
print('Printing cc1 object: ', cc1)
print('cc1 account owner name: ', cc1.getOwner_Name())
print('cc1 account owner address: ', cc1.getAddress())
print('cc1 card number: ', cc1.getCardNumber())
print('cc1 current balance: ', cc1.getBalance())
print('cc1 credit limit: ', cc1.getCreditLimit())
cc1.setCreditLimit(45)
print('cc1 setting new credit limit - 45: ', cc1.getCreditLimit())
print('cc1 makeCharge: 100')
cc1.makeCharge(100)
print('cc1 current balance: ', cc1.getBalance())
print('cc1 payBalance: 50')
cc1.payBalance(50)
print('cc1 current balance: ', cc1.getBalance())
print()

print('Creating CC, cc2, with Person p, num: 1234567890, balance: 0, limit: 1000')
num = 1234567890
bal = 0
limit = 1000
cc2 = CreditCard(p, num, bal, limit)
print('Printing cc2 object: ', cc2)
print('cc2 account owner name: ', cc2.getOwner_Name())
print('cc2 account owner address: ', cc2.getAddress())
print('cc2 card number: ', cc2.getCardNumber())
print('cc2 current balance: ', cc2.getBalance())
print('cc2 credit limit: ', cc2.getCreditLimit())
print('cc2 makeCharge(100)')
cc2.makeCharge(100)
print('cc2 current balance: ', cc2.getBalance())
print('cc2 payBalance(50)')
cc2.payBalance(50)
print('cc2 current balance: ', cc2.getBalance())
cc2.setCreditLimit(45)
print('cc2 setting new credit limit - setCreditLimit(45): ', cc2.getCreditLimit())
print('cc2 makeCharge(100)')
cc2.makeCharge(100)
print('cc2 current balance: ', cc2.getBalance())
print('cc2 payBalance(50)')
cc2.payBalance(50)
print('cc2 current balance: ', cc2.getBalance())
print('Trying to set credit limit to negative value. ')
cc2.setCreditLimit(-0.1)
print('cc2 current balance: ', cc2.getBalance())
print()
'''
Created on Jul 1, 2016

@author: Matt Wunschel
'''

class BankAccount(object):
    '''
    classdocs
    '''


    def __init__(self, balance):
        self.balance = balance
        self.info = []
        
    def deposit(self, amount):
        self.balance += amount
        self.info.append("Deposit: " + str(amount))
        print("Your new balance is " + str(self.balance))
        
    def widthdraw(self, amount):
        self.balance -= amount
        self.info.append("Withdraw: " + str(amount))
        print("Your new balance is " + str(self.balance))
        
    def createReciept(self):
        fw = open('reciept.txt', 'w')
        for x in self.info:
            fw.write(x + '\n')
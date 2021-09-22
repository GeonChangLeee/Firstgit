import sys
class atm:

    def __init__(self, name=None, accountNumber=None, balance=0):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount

    def withdrawal(self, amount):
        self.amount = amount
        self.balance = self.balance - amount

    def remittance(self, bank, accountNumber, amount):
        self.bank = bank
        self.accountNumber = accountNumber
        self.amount = amount
        self.balance = self.balance - amount
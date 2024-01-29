import ZODB, ZODB.config
import persistent
from abc import ABC, abstractmethod

class Customer(persistent.Persistent):
    def __init__(self, name = ""):
        self.name = name
        self.accounts = persistent.list.PersistentList()

    def __str__(self) -> str:
        return "Customer: " + self.name
    
    def setName(self, name):
        self.name = name
    
    def addAccount(self, account):
        self.accounts.append(account)
        return account
    
    def getAccounts(self, n):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None
    
    def printStatus(self):
        print(self.__str__())
        for account in self.accounts:
            print("", end="     ")
            account.printStatus()

class Account(ABC):
    def __init__(self, balance = 0.0, owner = None):
        self.balance = balance
        self.owner = owner
        self.transactions = persistent.list.PersistentList()

    @abstractmethod
    def __str__(self) -> str:
        return super().__str__()
    
    def accountDetails(self):
        return self.__str__()
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(
            BankTransaction(amount, self.balance, self.balance - amount, "Deposit")
        )

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(
            BankTransaction(amount, self.balance, self.balance + amount, "Withdraw")
        )

    def transfer(self, amount, account):
        self.balance -= amount
        self.transferIn(amount, account)
        self.transactions.append(
            BankTransaction(amount, self.balance, self.balance + amount, 
                            "Transfer to " + account.owner.name)
        )
    
    def transferIn(self, amount, account):
        account.balance += amount
        account.transactions.append(
            BankTransaction(amount, account.balance, account.balance - amount, 
                            "Transfer from " + self.owner.name)
        )

    def getBalance(self):
        return self.balance

    def printStatus(self):
        print(self.accountDetails())

    def printTransaction(self):
        for transaction in self.transactions:
            print("", end="     ")
            print(transaction)

class SavingsAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None):
        super().__init__(balance, owner)
        self.interest = 1.0

    def __str__(self) -> str:
        return f'Savings Account of Customer : {self.owner.name}   Balance: {self.balance}  Interest: {self.interest}'
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            return super().withdraw(amount)
        
class CurrentAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None):
        super().__init__(balance, owner)
        self.limit = -5000.0

    def __str__(self) -> str:
        return f'Current Account of Customer : {self.owner.name}   Balance: {self.balance}  Interest: {self.limit}'
    
    def withdraw(self, amount):
        # if self.amount > self.limit :
        #     print("Insufficient funds")
        # else:
            return super().withdraw(amount)

import datetime

class BankTransaction(persistent.Persistent):
    def __init__(self, amount, new_balance, old_balance, ttype):
        self.amount = amount
        self.new_balance = new_balance
        self.old_balance = old_balance
        self.timestamp = datetime.datetime.now()
        self.ttype = ttype

    def __str__(self) -> str:
        return f'''{self.ttype}  
        Amount: {self.amount}  
        Old Balance: {self.old_balance}  
        New Balance: {self.new_balance}  
        Timestamp: {self.timestamp}'''
    
    def printTransaction(self):
        print(self.__str__())
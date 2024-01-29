import ZODB, ZODB.config
import persistent
from abc import ABC, abstractmethod
import BTrees.OOBTree
import transaction
import z_obj

path = './config.xml'

db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root

if __name__ == "__main__":
    root.customer = BTrees.OOBTree.BTree()
    root.customer["Dave"] = z_obj.Customer("Dave")
    d = root.customer["Dave"]
    root.customer["John"] = z_obj.Customer("John")
    j = root.customer["John"]

    print("Create Accounts:")
    b1 = d.addAccount(z_obj.SavingsAccount(400, d))
    b2 = j.addAccount(z_obj.CurrentAccount(200, j))
    d.printStatus()
    j.printStatus()

    print("\nDeposit: 500 to Account 2")
    b2.deposit(500)
    b2.printStatus()

    print("\nWithdraw: 200 from Account 1")
    b1.withdraw(200)
    b1.printStatus()

    print("\nTransfer: 150 from Account 2 to Account 1")
    b2.transfer(150, b1)
    b1.printStatus()
    b2.printStatus()

    transaction.commit()






    # transaction.commit()
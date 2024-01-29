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
    for customer in root.customer:
        obj = root.customer[customer]
        obj.printStatus()
        print()
        index = 0
        while obj.getAccounts(index) != None:
            obj.getAccounts(index).printTransaction()
            print()
            index += 1
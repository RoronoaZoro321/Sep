import ZODB, ZODB.config
path = './config.xml'
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root
# print(root)
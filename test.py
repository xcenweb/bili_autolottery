import util.database

util.database.insert_user(1, 'test', 'test', 1)
if not util.database.exist_user(1):
    print(1)
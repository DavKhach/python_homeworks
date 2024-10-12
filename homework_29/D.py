"""Bad Example"""

# class MySQLDatabase:
#     def connect(self):
#         return "Connecting to MySQL database"
#
# class Order:
#     def __init__(self):
#         self.db = MySQLDatabase()
#
#     def save(self):
#         print(self.db.connect())
#         print("Saving order to MySQL database")


"""The order class is tightly coupled to MySQLDatabase,
making it hard to switch to another database"""


"""Right Example"""

class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL database"

class PostgresSQLDatabase(Database):
    def connect(self):
        return "Connecting to PostgresSQL database"

class Order:
    def __init__(self, database: Database):
        self.db = database

    def save(self):
        print(self.db.connect())
        print("Saving order in database")

mysql_db = MySQLDatabase()
postgres_db = PostgresSQLDatabase()

order1 = Order(mysql_db)
order1.save()

order2 = Order(postgres_db)
order2.save()

"""Now Order class depends on Database abstraction, making it easy
to switch between databases by passing the appropriate object"""

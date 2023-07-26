import sqlite3
from enum import Enum

cursor = sqlite3.connect(
    r'C:\Users\vadym.shurkhal\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db').cursor()


# cursor.execute("CREATE TABLE Data(data_id INTEGER PRIMARY KEY, name TEXT, data INTEGER CHECK(data<10));")
# cursor.execute("INSERT INTO Data(name, data) VALUES ('Hello', 3);")
# cursor.execute("CREATE TABLE Vendors(vendor_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, item TEXT, deal INTEGER, price REAL);")
# cursor.execute("CREATE TABLE Customers(customer_id INTEGER PRIMARY KEY, name TEXT NOT NULL, vendor_name TEXT, deal INTEGER, money REAL);")
# cursor.execute("INSERT INTO Customers(name, vendor_name, deal, money) VALUES ('Johnny', 'Johny', 3, 324234.4);")
# cursor.execute("INSERT INTO Customers(name, vendor_name, deal, money) VALUES ('Anna', 'Johny', 5, 324234.4);")
# cursor.execute("INSERT INTO Customers(name, money) VALUES ('Andrew', 324234.4);")
# cursor.execute("INSERT INTO Vendors(name, item, deal, price) VALUES ('Olaf', 'Car', 3, 14.4);")
# cursor.execute("INSERT INTO Vendors(name, item, deal, price) VALUES ('John', 'Train', 3, 14.4), ('Jerom', 'Tram', 1, 2.4), ('Anna', 'Plane', 7, 100),('Igor', 'Helicopter', 11, 1200);")

class DbQuery(str, Enum):
    SELECT_FROM = 'SELECT {} FROM {}'
    SELECT_FROM_WHERE = 'SELECT {} FROM {} WHERE {}'


cursor.execute(DbQuery.SELECT_FROM_WHERE.format('FirstName', 'Customer', 'SupportRepId>=4'))
all_result = cursor.fetchall()
for item in all_result:
    print(item)

# print(all_result)
# con.commit()
cursor.close()

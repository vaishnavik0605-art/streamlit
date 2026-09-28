import mysql.connector
class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con = mysql.connector.connect(
            user="root", password="123456789", host="localhost", database="librarydb"
        )
        print(self.con)
        self.cursor = self.con.cursor()
        print("Successfully connected")
    def list(self):
        # Reading all records from tsble
        query = 'select * from bookes'
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No records found")

    def create(self,title,author,price,pages,language):
        query = 'insert into bookes(title,author,price,pages,language) values(%s,%s,%s,%s,%s);'
        data = (title,author,price,pages,language)
        self.cursor.execute(query, data)
        self.con.commit()
        print("New record inserted successfully")

    def retrieve(self,id):
        # for reading a specific record
        query = 'select * from bookes where id = %s'
        data = (id,)
        self.cursor.execute(query,data)
        records = self.cursor.fetchone()
        if records:
            print(records)
        else:
            print('No records found')

    def update(self,id,title,author,price,pages,language):
        query = 'update bookes set title = %s, author = %s, price = %s, pages = %s, language = %s where id = %s'
        data = (title,author,price,pages,language,id,)
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            print('Updated')
        else:
            print("No records found")

    def delete(self,id):
        query = 'delete from bookes where id = %s'
        data = (id,)
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            print('Deleted')
        else:
            print("No records found")

book = BookListCreateRetrieveUpdateDelete()
book.list()
book.create('Malgudi Days', 'R.K. Narayan', 299.00, 256, 'English')
book.retrieve(1)
book.update(4,title='The Lost Symbol',author='Dan Brown',price=575.00,pages=509,language='English')
book.delete(id=3)
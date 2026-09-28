import mysql.connector
class DonorCRUD:
    def __init__(self):
        self.con = mysql.connector.connect(
            user="root", password="123456789", host="localhost", database="blooddb"
        )
        print(self.con)
        self.cursor = self.con.cursor()
        print("Successfully connected")
    def get(self):
        query = 'select * from donor'
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            return records
        else:
            print("No records found")
    def post(self,name,blood,phone,city,last_don):
        query = 'insert into donor(name,bloodgroup,phone,city,last_donation) values(%s,%s,%s,%s,%s);'
        data = (name,blood,phone,city,last_don)
        self.cursor.execute(query, data)
        self.con.commit()
        print("New record inserted successfully")
    # def retrieve(self,id):
    #     # for reading a specific record
    #     query = 'select * from donor where id = %s'
    #     data = (id,)
    #     self.cursor.execute(query,data)
    #     records = self.cursor.fetchone()
    #     if records:
    #         return records
    #     else:
    #         print('No records found')
    def put(self,id,name,blood,phone,city,last_don):
        query = 'update donor set name = %s, bloodgroup = %s, phone = %s, city = %s, last_donation = %s where id = %s'
        data = (name,blood,phone,city,last_don,id,)
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        else:
            return False
    def delete(self,id):
        query = 'delete from donor where id = %s'
        data = (id,)
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        else:
            return False

# donor = DonorCRUD()
# donor.get()
# donor.create('')
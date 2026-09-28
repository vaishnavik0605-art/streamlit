import mysql.connector
class DonorCRUD:
    def __init__(self):
        self.con = mysql.connector.connect(
            user="root", password="root", host="localhost", database="blood_db"
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


    def post(self,name,blood_group,phone,city,last_donation):
        query = 'insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s);'
        data = (name,blood_group,phone,city,last_donation)
        self.cursor.execute(query, data)
        self.con.commit()
        print("New record inserted successfully")



    def retrieve(self,id):
        # for reading a specific record
        query = 'select * from donor where id = %s'
        data = (id,)
        self.cursor.execute(query,data)
        records = self.cursor.fetchone()
        if records:
            return records
        else:
            print('No records found')


    def put(self,name,blood_group,phone,city,last_donation,id):
        query = 'update donor set name = %s, blood_group = %s, phone = %s, city = %s, last_donation = %s where id = %s'
        data = (name,blood_group,phone,city,last_donation,id,)
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
#
# # donor = DonorCRUD()
# # donor.get()
# # donor.create('')
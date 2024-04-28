#installed library mysql-connector-python
import mysql.connector
#creating connection
class delete:
    def _init_(self):

        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="#ajay@#$2811",
            database="bank"
            )
    def specific_delete(self,table_name,cusid):
        cur=self.conn.cursor()
        cur.execute(f"delete from {table_name} where customerID={cusid}")
        self.conn.commit()
        print("-----------deleted sucessfully-----------")
from multiprocessing import connection
from kivymd.app import MDApp
from kivy.lang import Builder
import mysql.connector


class SQLLite(MDApp):
    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Lime"

        # create database or connect to one
        mydb = mysql.connector.connect(
            host="localhost",
            user='root',
            password="root",
            database="second_db"
        )
        # create a cursor
        c = mydb.cursor()
        # create an actual database
        c.execute("CREATE DATABASE if not exists second_db ")

        # Check to see if database was created
        c.execute('SHOW DATABASES')
        for db in c:
            print(db)
        c.execute("USE second_db")

        # Create a table
        c.execute("CREATE TABLE if not exists customers(name VARCHAR(50))")

        # # cHECK TO SEE IF TABLE CREATED
        # c.execute("SELECT  * FROM customers")
        # print(c.description)
#
        mydb.commit()

        mydb.close()

        return Builder.load_file('main.kv')

    def fSubmit(self):
        # create database or connect to one
        mydb = mysql.connector.connect(
            host="localhost",
            user='root',
            password="root",
            database="second_db"
        )
        # create a cursor
        c = mydb.cursor()

        # add a records from customerss
        sql_cmd = "INSERT INTO customers (name) VALUES (%s)"
        values = (self.root.ids.word_input.text,)

        # Execute th command
        c.execute(sql_cmd, values)
        # Add title in the message
        self.root.ids.word_label.text = f"{self.root.ids.word_input.text}"

        # clear the input
        self.root.ids.word_input.text = ""
        mydb.commit()

        mydb.close()

    def fShowDetails(self):
        # create database or connect to one
        mydb = mysql.connector.connect(
            host="localhost",
            user='root',
            password="root",
            database="second_db"
        )
        # create a cursor
        c = mydb.cursor()

        # Grab records from customerss
        c.execute('SELECT * FROM customers')

        records = c.fetchall()
        word = ''
        for record in records:
            word = f"{word}\n{record[0]}"
            self.root.ids.word_label.text = f"{word}"

        mydb.commit()

        mydb.close()


if __name__ == "__main__":
    SQLLite().run()

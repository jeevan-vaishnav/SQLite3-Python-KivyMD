from multiprocessing import connection
from kivymd.app import MDApp
from kivy.lang import Builder
import sqlite3


class SQLLite(MDApp):
    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Lime"

        # Create Database or Connect to one
        con = sqlite3.connect("myfirstdb.db")
        # Create a cursor
        c = con.cursor()
        # Create a table
        c.execute("""
            CREATE TABLE if not exists customers(
                name text
            )
        """)

        # Commit our changes
        con.commit()

        # Close the connection
        con.close()

        return Builder.load_file('main.kv')

    def fSubmit(self):
        # Create Database or Connect to one
        con = sqlite3.connect("myfirstdb.db")
        # Create a cursor
        c = con.cursor()
        # Add A Record
        c.execute("INSERT INTO customers VALUES (:first)", {
            'first': self.root.ids.word_input.text,
        })

        # Add a title msg
        self.root.ids.word_label.text = f"{self.root.ids.word_input.text}"
        # Clear in the title
        self.root.ids.word_input.text = ""
        # Commit our changes
        con.commit()

        # Close the connection
        con.close()

    def fShowDetails(self):
        # Create Database or Connect to one
        con = sqlite3.connect("myfirstdb.db")
        # Create a cursor
        c = con.cursor()
        # Add A Record
        c.execute("SELECT * FROM customers ")
        records = c.fetchall()

        words = ""
        for record in records:
            words = f"{words}\n{record[0]}"
            self.root.ids.word_label.text = f"{words}"

        con.commit()
        con.close()


if __name__ == "__main__":
    SQLLite().run()

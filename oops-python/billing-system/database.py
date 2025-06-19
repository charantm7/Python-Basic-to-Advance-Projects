import sqlite3
from datetime import datetime

class BillingDB:
    def __init__(self):
        self.connect = sqlite3.connect('billing.db')
        self.create_table()
        self.cur = self.connect.cursor()

    def create_table(self):
        self.connect.execute(
            """
        CREATE TABLE IF NOT EXISTS PRODUCTS(product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT, 
        category TEXT,
        price INTEGER,
        quantity INTEGER)
        
        """
        )

        self.connect.execute(
            """
        CREATE TABLE IF NOT EXISTS CUSTOMER(customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone INTEGER,
        email TEXT)
        """
        )

        self.connect.execute(
            """
        CREATE TABLE IF NOT EXISTS BILL(bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER, data_time TEXT NOT NULL, total_price REAL NOT NULL, FOREIGN KEY (customer_id) REFERENCES CUSTOMER(customer_id)
        )
        """
        )

        self.connect.execute(
        
        """
        CREATE TABLE IF NOT EXISTS BILL_ITEM(items_id INTEGER PRIMARY KEY AUTOINCREMENT, bill_id INTEGER, product_id INTEGER, quantity INTEGER NOT NULL, price REAL NOT NULL, 
        FOREIGN KEY (bill_id) REFERENCES BILL(bill_id),
        FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id))
        """
        )

        self.connect.commit()

    def close(self):
        self.connect.close()

    def add_products(self, product_name, category, price, quantity):
        self.connect.execute("""
        INSERT INTO PRODUCTS( product_name, category, price, quantity) VALUES (?,?,?,?,?)
        """, ( product_name, category, price, quantity))
        self.connect.commit()
    
    def get_or_add_customers(self, name, phone, email ):
        self.connect.execute("""SELECT customer_id FROM CUSTOMER WHERE name = ?, phone = ?, email = ?""", (name, phone, email))
        result = self.cur.fetchone()
        if result:
            return result[0]
        else:
            self.connect.execute("""
            INSERT INTO CUSTOMER(name, phone, email)VALUES(?,?,?,?)
            """, (name, phone, email))
            self.connect.commit()
            return self.cur.lastrowid


    def create_bill(self, customer_id, total_price):
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.connect.execute("""
        INSERT INTO BILL(customer_id, date_time, total_price)
        """, (customer_id, date_time, total_price))
        self.connect.commit()
        self.cur.lastrowid

    def bill_for_items(self, bill_id, product_id, quantity, price):
        self.connect.execute("""
        SELECT price, quantity FROM PRODUCTS WHERE product_id = ?
        """, (product_id))

        prod
        self.connect.execute("""
        INSERT INTO BILL(bill_id, product_id, quantity, price)
        """, (bill_id, product_id, quantity, price))
        self.connect.commit()




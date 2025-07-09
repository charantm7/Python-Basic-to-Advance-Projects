import sqlite3
from datetime import datetime

class BillingDB:
    def __init__(self):
        self.connect = sqlite3.connect('billing.db')
        self.create_table()
        self.cur = self.connect.cursor()

    def create_table(self):
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS PRODUCTS(product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT, 
        category TEXT,
        price INTEGER,
        quantity INTEGER)
        
        """
        )

        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS CUSTOMER(customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone INTEGER,
        email TEXT)
        """
        )

        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS BILL(bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER, data_time TEXT NOT NULL, total_price REAL NOT NULL, FOREIGN KEY (customer_id) REFERENCES CUSTOMER(customer_id)
        )
        """
        )

        self.cur.execute(
        
        """
        CREATE TABLE IF NOT EXISTS BILL_ITEM(items_id INTEGER PRIMARY KEY AUTOINCREMENT, bill_id INTEGER, product_id INTEGER, quantity INTEGER NOT NULL, price REAL NOT NULL, 
        FOREIGN KEY (bill_id) REFERENCES BILL(bill_id),
        FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id))
        """
        )

        self.cur.commit()

    def close(self):
        self.cur.close()

    def add_products(self, product_name, category, price, quantity):
        self.cur.execute("""
        INSERT INTO PRODUCTS( product_name, category, price, quantity) VALUES (?,?,?,?,?)
        """, ( product_name, category, price, quantity))
        self.cur.commit()

    def view_products(self):
        products = self.cur.execute("""
        SELECT * FROM PRODUCTS
        """)
        return products.fetchall()
    
    def edit_products(self, product_id):
        print("What do want to edit?")
        print("1. All\n2. Name\n3. Price\n4. Stock Quantity\n5. Category\n6. Exit")
        choice = int(input("Enter the choice: "))

        if choice ==1:
            new_name = input("Enter the New Name: ")
            new_price = int(input("Enter the New Price: "))
            new_stock = int(input("Enter the New Stock Quantity: "))
            new_category = input("Enter the New category: ")

            self.cur.execute("""
            UPDATE PRODUCTS SET product_name=?, category=?, price=?, quantity=? WHERE product_id=?
            """,(new_name,new_category, new_price, new_stock, product_id))

        elif choice == 2:
            new_name = input("Enter the New Name: ")

            self.cur.execute("""
            UPDATE PRODUCTS SET product_name=? WHERE product_id=?
            """,(new_name, product_id,))
        
        elif choice == 3:
            new_price = int(input("Enter the New Price: "))

            self.cur.execute("""
            UPDATE PRODUCTS SET   price=? WHERE product_id=?
            """,( new_price, product_id,))

        elif choice == 4:
            new_stock = int(input("Enter the New Stock Quantity: "))

            self.cur.execute("""
            UPDATE PRODUCTS SET quantity=? WHERE product_id=?
            """,(new_stock, product_id,))

        elif choice == 5:
            new_category = input("Enter the New category: ")

            self.cur.execute("""
            UPDATE PRODUCTS SET category=? WHERE product_id=?
            """,(new_category, product_id,))
        
        elif choice == 6:
            print("Exiting...")
            return None
        else:
            print("Invalid Choice!")
            return
        
        self.cur.commit()


    def delete_product(self, product_id):
        self.cur.execute("""SELECT * FROM PRODUCTS WHERE product_id=?""", (product_id,))
        fetched = self.cur.fetchone()

        if not fetched:
            print(f"No product with this id: {product_id}")

        else:
            self.cur.execute("""DELETE FROM PRODUCTS WHERE product_id=?""", (product_id,))
            print(f"Product with id: {product_id} has Deleted!")

        self.cur.commit()


    def get_or_add_customers(self, name, phone, email ):
        self.cur.execute("""SELECT customer_id FROM CUSTOMER WHERE name = ?, phone = ?, email = ?""", (name, phone, email))
        result = self.cur.fetchone()
        if result:
            return result[0]
        else:
            self.cur.execute("""
            INSERT INTO CUSTOMER(name, phone, email)VALUES(?,?,?,?)
            """, (name, phone, email))
            self.cur.commit()
            return self.cur.lastrowid
        
    def view_all_customers(self):
        fetch = self.cur.execute("""SELETCT * FROM CUSTOMER""")
        return fetch.fetchall()

        # billing


    def create_bill(self, customer_id, total_price):
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cur.execute("""
        INSERT INTO BILL(customer_id, date_time, total_price)
        """, (customer_id, date_time, total_price))
        self.cur.commit()
        return self.cur.lastrowid

    def bill_for_items(self, bill_id, product_id, total_quantity):
        self.cur.execute("""
        SELECT price, quantity FROM PRODUCTS WHERE product_id = ?
        """, (product_id))
        product = self.cur.fetchone()

        if not product:
            print("No product available!")

        if total_quantity > quantity:
            print("No Available stocks")


        price , quantity = product
        
        total_price = total_quantity * price
       
        self.cur.execute("""
        INSERT INTO BILL(bill_id, product_id, quantity, price)
        """, (bill_id, product_id, total_quantity, total_price))
        self.cur.commit()
        
        new_stock = quantity - total_quantity

        self.cur.execute("""
                             UPDATE PRODUCTS SET quantity=? WHERE product_id=?""",(new_stock, product_id))

        self.cur.commit()

    def view_past_bill(self):
        last = self.cur.execute("""SELECT * FROM BILL ORDER BY bill_id DESC LIMIT 1""")
        return last.fetchone()
    

    def list_low_stock_product(self):
        print("1. Enter my own threshold to check stock quantity.")
        print("2. Give last 10 product which has low stock.")
        choice = int(input("Enter your choice [1,2]: "))

        if choice == 1:
            threshold = int(input("Enter the threshold number: "))
            return self.cur.execute("""SELECT * FROM PRODUCTS WHERE quantity < ?""", (threshold,)).fetchall()

        elif choice == 2:
            return self.cur.execute("""SELECT * FROM PRODUCTS ORDER BY quantity ASC LIMIT 10""")
        
        else:
            print("Inavlid choice!")
            return
        
        
            

        
    









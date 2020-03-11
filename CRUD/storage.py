import sqlite3

print("################################")
print("######## STORAGE SYSTEM ########")
print("################################")

print("# OPTIONS: ")
print("# 1 -> Create New Items.")
print("# 2 -> Read Items.")
print("# 3 -> Update Items.")
print("# 4 -> Delete Items.")
print("# 5 -> Exit.")
user_option = int(input("Select your option: "))
# if there is no database, python will create a new database
conn = sqlite3.connect("storage.db")


db_cursor = conn.cursor()

# create table
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
);
""")

# insert values
def insert_products():
    db_cursor.execute("INSERT INTO products(name, price) VALUES (?, ?)",(item_name,item_price))
    conn.commit()
    print("Success")

# select items
def select_products():
    db_cursor.execute("SELECT * FROM products;")
    for line in db_cursor.fetchall():
        print(line)

# update items price
def update_products():
    db_cursor.execute("UPDATE products SET price = ? WHERE id = ?",(new_price, product_id))
    conn.commit()
    print("Success")

# delete items
def delete_products():
    db_cursor.execute("DELETE FROM products WHERE id = ?",(product_id))
    conn.commit()
    print("Delete success")

if user_option == 1:
    item_name = input("Insert item name: ")
    item_price = float(input("Insert item price: "))
    insert_products()

if user_option == 2:
    select_products()

if user_option == 3:
    product_id = int(input("Insert id of the product: "))
    new_price = float(input("Insert new price for product: "))
    update_products()

if user_option == 4:
    product_id = int(input("Insert id of the product that will be deleted: "))
    delete_products()


conn.close()
import sqlite3 as sql
def initialize_db():
    connection = sql.connect("products.db")
    cursor = connection.cursor()

    #create table with products
    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute("CREATE TABLE products (name TEXT, description TEXT, price FLOAT, stock INTEGER, imgpath TEXT)")
    cursor.execute("""INSERT INTO products (name, description, price, stock, imgpath) VALUES \
        ('Penne Pasta', 'Our most popular dish...', 21.99, 10, '/static/images/pasta.jpeg'), \
        ('Chicken Noodle Soup', 'A heartwarming soup made with...', 9.99, 10, '/static/images/soup.jpeg'), \
        ('Strawberry Shortcake Cake', 'A delicious slice of cake...', 4.99, 10, '/static/images/cake.jpeg')
    """)

    # Create empty transactions table
    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute("CREATE TABLE transactions (timestamp TEXT, productid INTEGER, value INTEGER)")

    # Commit the db changes
    connection.commit()


def get_cursor():
    connection = sql.connect("products.db")
    cursor = connection.cursor()
    return (cursor, connection)

#process information about all the products to be displayed
def process_info():
    (cursor, _) = get_cursor()
    cursor.execute("SELECT rowid, * FROM products")
    rows = cursor.fetchall()

    products = []
    for row in rows:
        products.append({
            "id":    row[0],
            "name":  row[1],
            "description": row[2],
            "price": "$%.2f" % (row[3]),
            "stock": "%d left" % (row[4]),
            "src":   "%s" % (row[5]),
        })
    return products

#get data on specific product
def get_product(product_id):
    (cursor, _) = get_cursor()
    cursor.execute("SELECT name, description, price, stock FROM products WHERE rowid = ?", (product_id,))
    result = cursor.fetchone()
    return result

#update information for specific product
def update_product(name, description, price, stock, product_id):
    (cursor, connection) = get_cursor()
    cursor.execute("UPDATE products SET name = ?, description = ?, price = ?, stock = ? WHERE rowid = ?", (name, description, price, stock, product_id,))
    connection.commit()

#process a buy transaction
def process_transaction(product_id, price):
    (cursor, connection) = get_cursor()
    cursor.execute("INSERT INTO transactions (timestamp, productid, value) VALUES " + \
    "(datetime(), ?, ?)", (product_id, price))

    cursor.execute("UPDATE products SET stock = stock - 1 WHERE rowid = ?", (product_id,))
    connection.commit()

#calculate the total earnings
def calc_sum():
    (cursor, connection) = get_cursor()
    cursor.execute("SELECT SUM(value) FROM transactions")
    result = cursor.fetchone()[0]
    earnings = result if result else 0
    return earnings

#delete item
def delete(product_id):
    (cursor, connection) = get_cursor()
    cursor.execute("DELETE FROM products WHERE rowid = ?", (product_id,))
    connection.commit()
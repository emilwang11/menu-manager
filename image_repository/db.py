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
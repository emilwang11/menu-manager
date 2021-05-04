from flask import Flask, render_template, request, url_for, redirect
import sqlite3 as sql
from image_repository import db
from .form import EditForm

def get_cursor():
    connection = sql.connect("products.db")
    cursor = connection.cursor()
    return (cursor, connection)

def process_info():
    (cursor, _) = get_cursor()
    cursor.execute("SELECT rowid, * FROM products")

    rows = cursor.fetchall()
    print("Retrieved %d database entries" % len(rows))

    # Pre-process product info for HTML templates
    products = []
    for row in rows:
        products.append({
            "id":    row[0],
            "name":  row[1],
            "description": row[2],
            "price": "$%.2f" % (row[3]/100.0),
            "stock": "%d left" % (row[4]),
            "src":   "%s" % (row[5]),
        })
    return products

@app.route("/")
def home_page():
    products = process_info()
    return render_template("index.html", products=products)

@app.route("/manage", methods=['GET', 'POST'])
def manage_page():
    products = process_info()

    (cursor, _) = get_cursor()

    # Display total sales so far
    cursor.execute("SELECT SUM(value) FROM transactions")
    result = cursor.fetchone()[0]
    earnings = result if result else 0

    return render_template("manage.html", products=products, earnings=earnings)

# @app.route("/edit/<product_id>")
# def edit(product_id):
#     return render_template("edit.html")
    # if request.method == 'POST':
    #     (cursor, connection) = get_cursor()
    #     cursor.execute(
    #         "UPDATE products SET name = ? WHERE rowid = ?", (name, product_id))
    #     connection.commit()

@app.route("/edit/<product_id>", methods=["GET", "POST"])
def edit(product_id):
    form = EditForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "edit.jinja2",
        form=form,
        template="form-template"
    )

@app.route("/buy/<product_id>")
def buy(product_id):
    if not product_id:
        return render_template("message.html", message="Invalid product ID!")

    (cursor, connection) = get_cursor()

    cursor.execute("SELECT rowid, price, stock FROM products WHERE rowid = ?", (product_id,))
    result = cursor.fetchone()

    if not result:
        return render_template("message.html", message="Invalid product ID!")
    (rowid, price, stock) = result

    if stock <= 0:
        return render_template("message.html", message="Insufficient stock!")

    print("Processed transaction of value $%.2f" % (price/100.0))
    cursor.execute("INSERT INTO transactions (timestamp, productid, value) VALUES " + \
        "(datetime(), ?, ?)", (rowid, price))

    cursor.execute("UPDATE products SET stock = stock - 1 WHERE rowid = ?", (product_id,))
    connection.commit()
    return render_template("message.html", message="Purchase successful!")


@app.route("/reset")
def reset():
    initialize_db()
    return render_template("message.html", message="Database reset.")

if __name__ == '__main__':
    initialize_db()
    app.run(debug = True)



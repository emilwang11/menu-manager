from flask import Flask, render_template, request, url_for, redirect
import sqlite3 as sql
from image_repository import app, db
from .form import EditForm

#home page to view and buy products
@app.route("/")
def home_page():
    products = db.process_info()
    return render_template("index.html", products=products)

#page to edit and delete products
@app.route("/manage", methods=['GET'])
def manage_page():
    products = db.process_info()

    (cursor, _) = db.get_cursor()
    earnings ="$%.2f" % db.calc_sum()

    # Display total sales
    return render_template("manage.html", products=products, earnings=earnings)

#delete product
@app.route("/delete/<product_id>")
def delete(product_id):
    db.delete(product_id)
    return render_template("message.html", message="Deletion successful!")

#form page to edit information about product
@app.route("/edit/<product_id>", methods=["GET", "POST"])
def edit(product_id):
    item_info = db.get_product(product_id)
    class item(object):
        def __init__(self):
            self.name = item_info[0]
            self.description = item_info[1]
            self.price = item_info[2]
            self.stock = item_info[3]
    form = EditForm(obj=item())

    if form.validate_on_submit():
        db.update_product(form.name.data, form.description.data, form.price.data, form.stock.data, product_id,)
        return redirect('/manage')

    return render_template(
        "edit.jinja2",
        form=form,
        product_id=product_id,
        template="form-template"
    )

#buy product
@app.route("/buy/<product_id>")
def buy(product_id):
    if not product_id:
        return render_template("message.html", message="Invalid product ID!")

    result = db.get_product(product_id)

    if not result:
        return render_template("message.html", message="Invalid product ID!")
    (price, stock) = (result[2], result[3])

    if stock <= 0:
        return render_template("message.html", message="Insufficient stock!")

    db.process_transaction(product_id, price)
    return render_template("message.html", message="Purchase successful!")

#reset values in the database
@app.route("/reset")
def reset():
    db.initialize_db()
    return render_template("message.html", message="Database reset.")





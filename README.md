# Menu Manager
## Shopify Fall 2021 Developer Intern Challenge

With the prompt of building an image repository, I decided to turn it into a menu where users can buy and manage products.

To run the application:
1. Clone the repo
2. `pip install .`
3. `python run.py`
4.  visit `http://127.0.0.1:5000/`

#### Home Page
As a customer,you are able to view the menu item's information and purchase it. Edge cases for purchases are handled such as insufficient stock and invalid product ID.

#### Manage Page
As an admin, you can:
1. Can edit the information (name, description, price and stock) about the items
2. Can delete products
3. Can view the amount of sales that have been made so far
4. Can reset the database to the default values

## Next Steps
1. I chose to use SQLite initially because of how lightweight it is, however this presented some limitations later on with database interactions. If I had more time, I would use SQLAlchemy since it has an ORM making data access more abstract and portable. Instead of using raw SQL queries I would be able to create models and mappings to objects.
2. Implement image upload feature so admins can change the image for the product as well as add new products


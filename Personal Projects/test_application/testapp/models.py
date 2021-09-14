"""sqlite3 classes for RichGuy and Product.

Robert Davis
2021/09/13"""


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class RichGuy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    networth = db.Column(db.Numeric, nullable=False)

    def __repr__(self):
        return f'RichGuy Object: {self.name}'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Product Object: {self.name}'

class Calculation():

    def __init__(self, richGuy, product):
        self.richGuy = richGuy.name
        self.netWorth = richGuy.networth
        self.product = product.name
        self.price = product.price

        self.amount = float(self.netWorth * 1000000) / self.price
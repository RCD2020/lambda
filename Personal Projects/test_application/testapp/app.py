"""My web application for tweets and stuff.

Robert Davis
2021/09/13"""


from flask import Flask, render_template, request
from .models import db, RichGuy, Product, Calculation
import os


app_dir = os.path.dirname(os.path.abspath(__file__))
database = f'sqlite:///{os.path.join(app_dir, "tweeter.sqlite3")}'


def create_app():
    """Creates application."""

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = database
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def indexPage():
        return render_template('index.html')

    @app.route('/eat_the_rich', methods=['GET', 'POST'])
    def richPage():
        name = request.form.get('name')
        networth = request.form.get('networth')

        if name:
            therich = RichGuy(name=name, networth=networth)
            db.session.add(therich)
            db.session.commit()

        dudes = RichGuy.query.all()
        return render_template('eat_the_rich.html', dudes=dudes)

    @app.route('/products', methods=['GET', 'POST'])
    def productPage():
        name = request.form.get('name')
        price = request.form.get('price')

        if name:
            product = Product(name=name, price=price)
            db.session.add(product)
            db.session.commit()

        products = Product.query.all()
        return render_template('products.html', products=products)

    @app.route('/calculator', methods=['GET', 'POST'])
    def calcPage():
        therich = request.form.get('richguyOut')
        theproduct = request.form.get('productOut')

        if therich == None:
            therich = 1
        else:
            therich = int(therich)
        if theproduct == None:
            theproduct = 1
        else:
            theproduct = int(theproduct)

        richDudes = RichGuy.query.all()
        products = Product.query.all()

        calculation = Calculation(
            richDudes[therich-1],
            products[theproduct-1]
        )

        return render_template('calculator.html', richDudes=richDudes, products=products, calculation=calculation)

    return app

"""My web application for tweets and stuff.

Robert Davis
2021/09/13"""


from flask import Flask, render_template, request
from .models import db, User, Tweet
import os


app_dir = os.path.dirname(os.path.abspath(__file__))
database = f'sqlite:///{os.path.join(app_dir, "tweeter.sqlite3")}'


def create_app():
    """Creates the application"""

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = database
    app.config['SQLALCHEMY_TRACK_NOTFICATIONS'] = False

    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/users', methods=['GET', 'POST'])
    def usersPage():
        name = request.form.get('name')

        if name:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()

        users = User.query.all()
        return render_template('users.html', users=users)

    @app.route('/tweets', methods=['GET', 'POST'])
    def tweetsPage():
        userid = request.form.get('userid')
        twet = request.form.get('tweet')

        if twet:
            tweet = Tweet(text=twet, userid=userid)
            db.session.add(tweet)
            db.session.commit()

        users = User.query.all()
        tweets = Tweet.query.all()
        return render_template(
            'tweets.html',
            users=users,
            tweets=tweets
        )

    return app

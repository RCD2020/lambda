"""My web application for pulling twitter users and tweets.

Robert Davis
2021/09/14"""


from flask import Flask, render_template, request
from .models import db, User, Tweet
import tweepy
import spacy
import en_core_web_sm
import os


app_dir = os.path.dirname(os.path.abspath(__file__))
database = f'sqlite:///{os.path.join(app_dir, "twitter.sqlite3")}'
nlp_model = en_core_web_sm.load()


def retrieve_keys(
    path='/Users/colby/Documents/Lambda/03 Unit 3/twitterapi.keys'
):
    """Retrieves my twitter api keys because .env files won't work"""

    file = open(
        '/Users/colby/Documents/Lambda/03 Unit 3/twitterapi.keys',
        'r'
    )

    data = file.read().split('\n')

    keys = {}

    for x in data:
        y = x.split('=')

        keys[y[0]] = y[1]

    return keys


def twit_connect(keys=retrieve_keys()):
    """Connects to twitter. Returns a tweepy.API object."""

    auth = tweepy.OAuthHandler(keys['KEY'], keys['SECRET'])
    twitter = tweepy.API(auth)

    return twitter


def create_app():
    """Creates the application"""

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = database
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    twitter = twit_connect()


    @app.route('/')
    def indexPage():
        return render_template('index.html')

    @app.route('/users', methods=['GET', 'POST'])
    def usersPage():
        name = request.form.get('name')
        message = ['' for x in range(1)]
        users = User.query.all()

        if name:
            try:
                twituser = twitter.get_user(name)

                user = User(name=name)
                tweets = twituser.timeline(
                    count=3, exclude_replies=True,
                    include_rts=False, tweet_mode='Extended'
                )

                for tweet in tweets:
                    tweetObj = Tweet(userid=users[-1].id+1,
                        text=tweet.text)
                    db.session.add(tweetObj)

                db.session.add(user)
                message[0] = f'Added user @{name} successfully'
                db.session.commit()
            except:
                message[0] = f'Could not find user @{name}'

        users = User.query.all()
        return render_template(
            'users.html', users=users,
            message=message)

    @app.route('/tweets', methods=['GET', 'POST'])
    def tweetsPage():
        users = User.query.all()
        tweets = Tweet.query.all()
        vector = request.form.get('vector')

        if vector:
            vectored = nlp_model(tweets[int(vector)-1].text).vector
        else:
            vectored = 'Vector will appear here.'

        return render_template('tweets.html',
            users=users, tweets=tweets, vector=vectored)

    return app

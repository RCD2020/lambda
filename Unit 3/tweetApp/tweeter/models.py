"""Python Classes for Tweet and User.

Robert Davis
2021/09/13"""


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User: {self.name}>'


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(280), nullable=False)

    def __repr__(self):
        return f"<Tweet: {self.text}>"
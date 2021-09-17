"""OpenAQ Air Quality Dashboard with Flask.

Robert Davis
2021/09/17"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq


APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)
API = openaq.OpenAQ()


rootHTML = """<h1>Potentially Risky</h1>
<p><a href=\"/refresh\">Refresh data</a></p>
<p>{}</p>"""


refreshHTML = """<h3>Data refreshed!</h3>
<p><a href=\"/\">Back</a></p>"""


class Record(DB.Model):
    """Record Class for storing dates and air quality values."""

    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f'Record {self.datetime}: {self.value}'


def get_results():
    """Pulls data from OpenAQ Los Angeles (pm25) and converts it into
    timedate and value pairs.
    Returns list of (timedate, value) tuples."""

    s, body = API.measurements(city='Los Angeles', parameter='pm25')

    timeval = [(x['date']['utc'], x['value']) for x in body['results']]

    return timeval


@APP.route('/')
def root():
    """Base view."""

    risky = Record.query.filter(Record.value >= 10).all()

    riskyHTML = """<ul>
"""

    for entry in risky:
        riskyHTML += f"""    <li>{entry}</li>
"""

    riskyHTML += """</ul>"""

    return rootHTML.format(riskyHTML)


@APP.route('/refresh')
def refresh():
    """Pull fresh data from OpenAQ and replace existing data."""

    DB.drop_all()
    DB.create_all()
    data = [Record(datetime=x[0], value=x[1]) for x in get_results()]
    for record in data:
        DB.session.add(record)
    DB.session.commit()

    return refreshHTML

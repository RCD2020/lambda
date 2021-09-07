"""Uploads the titanic dataset to PostgreSQL database.

Robert Davis
2021/09/07"""


import sys
import pandas as pd
import psycopg2


dbname = 'afedwtui'
user = 'afedwtui'
host = 'kashin.db.elephantsql.com'


def tit_init(cur):
    """Creates the tables for the titanic database."""

    # Create Gender Enumerator
    gender = """CREATE TYPE gender AS ENUM ('male', 'female')"""

    # Passenger Table
    passenger = """CREATE TABLE passenger (
id SERIAL PRIMARY KEY,
survived BOOLEAN,
pclass INTEGER,
fare NUMERIC)"""

    # Personal Info Table
    personal = """CREATE TABLE personal (
id SERIAL PRIMARY KEY,
name VARCHAR(255),
sex gender,
age INTEGER,
sibSpouseAboard INTEGER,
parentsChildsAboard INTEGER)"""

    cur.execute(gender)
    cur.execute(passenger)
    cur.execute(personal)


def upload(con, cur, df):
    """Uploads the titanic dataframe to the PostgreSQL server."""

    passengers = df[['Survived', 'Pclass', 'Fare']].itertuples()
    personal = df[[
        'Name',
        'Sex',
        'Age',
        'Siblings/Spouses Aboard',
        'Parents/Children Aboard'
    ]].itertuples()

    passersSQL = 'INSERT INTO passenger (survived, pclass, fare) \
VALUES (%s, %s, %s)'

    for rows in passengers:
        cur.execute(
            passersSQL,
            (bool(rows[1]), rows[2], rows[3])
        )
    
    persSQL = 'INSERT INTO personal (name, sex, age, sibSpouseAboard, \
parentsChildsAboard) VALUES (%s, %s, %s, %s, %s)'

    for row in personal:
        cur.execute(
            persSQL,
            (row[1], row[2], row[3], row[4], row[5])
        )

    con.commit()
        


if __name__ == '__main__':
    con = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=sys.argv[1],
        host=host
    )

    cur = con.cursor()

    # Creates the tables
    tit_init(cur)

    # Upload the data
    df = pd.read_csv('/Users/colby/Documents/Lambda/03 Unit 3/lambda/\
Unit 3/titanic/titanic.csv')

    # upload(con, cur, df)

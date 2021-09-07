"""Creates holidaymove_buddyiq.sqlite3

Robert Davis
2021/09/07"""


import pandas as pd
import sqlite3


PATH = '/Users/colby/Documents/Lambda/03 Unit 3/\
lambda/Unit 3/rpg/buddymove_holidayiq.csv'


ROW_COUNT = """SELECT COUNT(*) FROM review"""


SHOPNAT = """SELECT COUNT(*) FROM review
WHERE Nature>=100 AND Shopping>=100"""


AVERAGES = {
    'Sports': """SELECT AVG(Sports) FROM review""",
    'Religious': """SELECT AVG(Religious) FROM review""",
    'Nature': """SELECT AVG(Nature) FROM review""",
    'Theatre': """SELECT AVG(Theatre) FROM review""",
    'Shopping': """SELECT AVG(Shopping) FROM review""",
    'Picnic': """SELECT AVG(Picnic) FROM review"""
}


if __name__ == '__main__':
    df = pd.read_csv(PATH)

    con = sqlite3.connect('/Users/colby/Documents/Lambda/03 Unit 3/\
lambda/Unit 3/rpg/rpgholidaymove_buddyiq.sqlite3')
    cur = con.cursor()

    df.to_sql('review', con=con)

    cur.execute(ROW_COUNT)
    for row in cur:
        print('\033[35mTotal Reviewers:\033[00m', row[0])

    cur.execute(SHOPNAT)
    for row in cur:
        print('\033[35mTotal Reviewers \033[36mwho reviewed 100 \
in Nature and Shopping:\033[00m', row[0])

    for cat, sql in AVERAGES.items():
        cur.execute(sql)
        for row in cur:
            print(f'\033[36mAverage Total {cat} Reviews:\
\033[00m {row[0]}')

    con.close()

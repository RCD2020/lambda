"""For Unit 3 Sprint 2 Part1;
a file that writes a demo_data.sqlite3 and analyzes the data a bit.

Robert Davis
2021/09/10"""


import sqlite3


TABLE = '''CREATE TABLE demo (
    s CHAR(1),
    x INT(2),
    y INT(2)
);'''


INSERTS = [
    "'g', 3, 9",
    "'v', 5, 7",
    "'f', 8, 7"
]


INSERTABLE = '''INSERT INTO demo
VALUES ({});'''


row_count = '''SELECT COUNT(*)
FROM demo'''


xy_at_least_5 = '''SELECT COUNT(*)
FROM demo
WHERE x >= 5 AND y >= 5;'''


unique_y = '''SELECT COUNT(DISTINCT y)
FROM demo;'''


def extract(cur, sql, text=None):
    '''Extracts the data from an execution and returns it.
    It can also print the results if you specify a text with braces in
    it.'''

    cur.execute(sql)
    for x in cur:
        data = x[0]

    if text is not None:
        print(text.format(data))

    return data


if __name__ == '__main__':
    # Make the database
    con = sqlite3.connect('/Users/colby/Documents/Lambda/03 Unit 3/\
lambda/Unit 3/Sprint 2/demo_data.sqlite3')
    cur = con.cursor()

    cur.execute(TABLE)

    for insert in INSERTS:
        cur.execute(INSERTABLE.format(insert))
    con.commit()

    # Read the database
    extract(cur, row_count, '\033[34mThere are {} rows.')
    extract(cur, xy_at_least_5, '\033[36mThere are {} \
rows where x and y are at least 5.')
    extract(cur, unique_y, '\033[34mThere are {} unique y \
values.')

    con.close()

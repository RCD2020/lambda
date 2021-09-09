"""Gets data from the Postgre database.

Robert Davis
2021/09/09"""


import sys
import psycopg2


def connect(
    password,
    dbname='afedwtui',
    user='afedwtui',
    host='kashin.db.elephantsql.com'
):
    """Connects to the database"""

    con = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host
    )
    cur = con.cursor()

    return con, cur


def data(cur, sql, title, color='\033[35m'):
    """Prints the data to the terminal, returns the data."""
    cur.execute(sql)
    for x in cur:
        point = x[0]
        print(f'{color}{title}:\033[00m', point)

    return point


TOTAL_SURVIVED = '''SELECT COUNT(*)
FROM passenger
WHERE survived = True;'''


TOTAL_DECEASED = '''SELECT COUNT(*)
FROM passenger
WHERE survived = False'''


TOTAL_CLASS = '''SELECT COUNT(*)
FROM passenger
WHERE pclass = {}'''


TOTAL_CLASS_SURVIVED = '''SELECT COUNT(*)
FROM passenger
WHERE pclass = {} AND survived = {}'''


AVERAGE_PERSONAL = '''SELECT AVG({})
FROM passenger
JOIN personal ON passenger.id=personal.id
WHERE {}'''


GROUPED = '''SELECT COUNT(*)
FROM personal
GROUP BY name'''


TOTAL = '''SELECT *
FROM personal'''


if __name__ == '__main__':
    con, cur = connect(sys.argv[1])

    data(cur, TOTAL_SURVIVED, 'Total Survived')
    data(
        cur,
        AVERAGE_PERSONAL.format('age', 'survived = True'),
        'Average Age',
        '\033[36m'
    )
    data(
        cur,
        AVERAGE_PERSONAL.format('fare', 'survived = True'),
        'Avergae Fare',
        '\033[36m'
    )
    data(
        cur,
        AVERAGE_PERSONAL.format('sibSpouseAboard', 'survived = True'),
        'Average Number of Siblings/Spouses',
        '\033[36m'
    )
    data(
        cur,
        AVERAGE_PERSONAL.format(
            'parentsChildsAboard',
            'survived = True'
        ),
        'Average Number of Parents/Children',
        '\033[36m'
    )

    data(cur, TOTAL_DECEASED, 'Total Deceased')
    data(
        cur,
        AVERAGE_PERSONAL.format('age', 'survived = False'),
        'Average Age',
        '\033[36m'
    )
    data(
        cur,
        AVERAGE_PERSONAL.format('fare', 'survived = False'),
        'Average Fare',
        '\033[36m'
    )
    data(
        cur,
        AVERAGE_PERSONAL.format('sibSpouseAboard', 'survived = False'),
        'Average Number of Siblings/Spouses',
        '\033[36m'
    )
    data(
        cur,
        AVERAGE_PERSONAL.format(
            'parentsChildsAboard',
            'survived = False'
        ),
        'Average Number of Parents/Children',
        '\033[36m'
    )

    for x in range(3):
        data(cur, TOTAL_CLASS.format(x+1), f'Total in Class {x+1}')
        data(
            cur,
            TOTAL_CLASS_SURVIVED.format(x+1, True),
            'Total Survived',
            '\033[36m'
        )
        data(
            cur,
            TOTAL_CLASS_SURVIVED.format(x+1, False),
            'Total Deceased',
            '\033[36m'
        )
        data(
            cur,
            AVERAGE_PERSONAL.format('age', f'pclass = {x+1}'),
            'Average Age',
            '\033[36m'
        )
        data(
            cur,
            AVERAGE_PERSONAL.format('fare', f'pclass = {x+1}'),
            'Average Fare',
            '\033[36m'
        )
        data(
            cur,
            AVERAGE_PERSONAL.format(
                'sibSpouseAboard',
                f'pclass = {x+1}'
            ),
            'Average Number of Siblings/Spouses',
            '\033[36m'
        )
        data(
            cur,
            AVERAGE_PERSONAL.format(
                'parentsChildsAboard',
                f'pclass = {x+1}'
            ),
            'Average Number of Parents/Children',
            '\033[36m'
        )

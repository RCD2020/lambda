"""Used for transferring the rpg_db.sqlite3 to a mongo server.
Pass the password as your second argument when running on console.

Robert Davis
2021/09/08"""


import pymongo
import sqlite3
import sys


def mongo_connect(
    password,
    user='RCD2021',
    dbname='myFirstDatabase'
):
    """Connects to the mongoDB. Pass through the password,
returns the db"""

    client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}\
@cluster0.z3tac.mongodb.net/{dbname}?retryWrites=true&w=majority")
    db = client.test

    return db


def lite_connect(path):
    """Connects to a sqlite3 file. Returns the connection and cursor."""

    con = sqlite3.connect(path)
    cur = con.cursor()

    return con, cur


RPG_TABLES = {
    'charactercreator_character': '''SELECT character_id, name, level, \
exp, hp, strength, intelligence, dexterity, wisdom
FROM charactercreator_character''',
    'charactercreator_character_inventory': '''SELECT id, character_id,\
 item_id
FROM charactercreator_character_inventory''',
    'armory_item': '''SELECT item_id, name, value, weight
FROM armory_item''',
    'armory_weapon': '''SELECT item_ptr_id, power
FROM armory_weapon'''
}


if __name__ == '__main__':
    db = mongo_connect(sys.argv[1])
    con, cur = lite_connect('/Users/colby/Documents/Lambda/03 Unit 3/\
lambda/Unit 3/rpg/rpg_db.sqlite3')

    for name, sql in RPG_TABLES.items():
        rows = cur.execute(sql).fetchall()
        columns = [d[0] for d in cur.description]

        table = [dict(zip(columns, row)) for row in rows]

        exec(f'db.{name}.insert_many(table)')

    print(db.list_collection_names())

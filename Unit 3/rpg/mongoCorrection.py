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


ITEMS = '''SELECT character_id,  name
FROM charactercreator_character_inventory
JOIN armory_item
ON charactercreator_character_inventory.item_id = armory_item.item_id
WHERE armory_item.item_id NOT IN \
(SELECT item_ptr_id FROM armory_weapon);'''


WEAPONS = '''SELECT character_id,  name
FROM charactercreator_character_inventory
JOIN armory_item
ON charactercreator_character_inventory.item_id = armory_item.item_id
WHERE armory_item.item_id IN \
(SELECT item_ptr_id FROM armory_weapon);'''


CHARACTERS = '''SELECT character_id, name, level, \
exp, hp, strength, intelligence, dexterity, wisdom
FROM charactercreator_character'''


if __name__ == '__main__':
    db = mongo_connect(sys.argv[1])
    con, cur = lite_connect('/Users/colby/Documents/Lambda/03 Unit 3/\
lambda/Unit 3/rpg/rpg_db.sqlite3')

    rows = cur.execute(CHARACTERS).fetchall()
    data = [[
        ide, name, level, exp, hp, stre, inte, dex, wis, [], []
    ] for ide, name, level, exp, hp, stre, inte, dex, wis in rows]
    columns = [d[0] for d in cur.description]
    columns.append('items')
    columns.append('weapons')
    
    rows = cur.execute(ITEMS).fetchall()
    for ide, name in rows:
        data[ide-1][9].append(name)

    rows = cur.execute(WEAPONS).fetchall()
    for ide, name in rows:
        data[ide-1][10].append(name)

    table = [dict(zip(columns[1:], row[1:])) for row in data]

    db.rpg.insert_many(table)

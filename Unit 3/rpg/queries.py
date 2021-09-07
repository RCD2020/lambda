"""Python file contained queries for rpd_db.sqlite3

Robert Davis
2021/09/07
"""


import sqlite3


def connect(path):
    con = sqlite3.connect(path)
    cur = con.cursor()

    return con, cur


TOTAL_CHARACTERS = """SELECT COUNT(name)
FROM charactercreator_character"""


TOTAL_SUBCLASS_CLERIC = """SELECT COUNT(character_ptr_id)
FROM charactercreator_cleric"""


TOTAL_SUBCLASS_FIGHTER = """SELECT COUNT(character_ptr_id)
FROM charactercreator_fighter"""


TOTAL_SUBCLASS_MAGE = """SELECT COUNT(character_ptr_id)
FROM charactercreator_mage"""


TOTAL_SUBCLASS_NECROMANCER = """SELECT COUNT(mage_ptr_id)
FROM charactercreator_necromancer"""


TOTAL_SUBCLASS_THIEF = """SELECT COUNT(character_ptr_id)
FROM charactercreator_thief"""


TOTAL_ITEMS = """SELECT COUNT(name)
FROM armory_item"""


TOTAL_WEAPONS = """SELECT COUNT(item_ptr_id)
FROM armory_weapon"""


TOTAL_NOT_WEAPONS = """SELECT COUNT(*) FROM armory_item
WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon)"""


CHARACTER_ITEMS = """SELECT character_id, COUNT(character_id)
FROM charactercreator_character_inventory
GROUP BY character_id
ORDER BY COUNT(character_id) DESC
LIMIT 20"""


CHARACTER_WEAPONS = """SELECT character_id, COUNT(character_id)
FROM charactercreator_character_inventory
WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
GROUP BY character_id
ORDER BY COUNT(character_id) DESC
LIMIT 20"""


AVG_CHARACTER_ITEMS = """SELECT AVG(iCount)
FROM
    (
    SELECT COUNT(character_id) as iCount
    FROM charactercreator_character_inventory
    GROUP BY character_id
    )"""


AVG_CHARACTER_WEAPONS = """SELECT AVG(wCount)
FROM
    (
    SELECT COUNT(character_id) as wCount
    FROM charactercreator_character_inventory
    WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
    GROUP BY character_id
    )"""


if __name__ == '__main__':
    path = '/Users/colby/Documents/Lambda/\
03 Unit 3/lambda/Unit 3/rpg/rpg_db.sqlite3'

    con, cur = connect(path)

    cur.execute(TOTAL_CHARACTERS)
    for row in cur:
        print('\033[35mTotal Characters:\033[00m', row[0])
    
    cur.execute(TOTAL_SUBCLASS_CLERIC)
    for row in cur:
        print('\033[36mTotal Clerics:\033[00m', row[0])

    cur.execute(TOTAL_SUBCLASS_FIGHTER)
    for row in cur:
        print('\033[36mTotal Fighters:\033[00m', row[0])

    cur.execute(TOTAL_SUBCLASS_MAGE)
    for row in cur:
        print('\033[36mTotal Mages:\033[00m', row[0])

    cur.execute(TOTAL_SUBCLASS_NECROMANCER)
    for row in cur:
        print('\033[36mTotal Necromancers:\033[00m', row[0])

    cur.execute(TOTAL_SUBCLASS_THIEF)
    for row in cur:
        print('\033[36mTotal Thieves:\033[00m', row[0])

    cur.execute(TOTAL_ITEMS)
    for row in cur:
        print('\033[35mTotal Items:\033[00m', row[0])

    cur.execute(TOTAL_WEAPONS)
    for row in cur:
        print('\033[36mTotal Weapons:\033[00m', row[0])

    cur.execute(TOTAL_NOT_WEAPONS)
    for row in cur:
        print('\033[36mTotal NonWeapon Items:\033[00m', row[0])

    print('\033[33mCharacter Total Items:\033[00m')
    cur.execute(CHARACTER_ITEMS)
    for row in cur:
        print(f"Character {row[0]}: {row[1]} items")

    print('\033[33mCharacter Total Weapons:\033[00m')
    cur.execute(CHARACTER_WEAPONS)
    for row in cur:
        print(f"Character {row[0]}: {row[1]} weapons")

    cur.execute(AVG_CHARACTER_ITEMS)
    for row in cur:
        print('\033[36mAverage Character Items:\033[00m', row[0])

    cur.execute(AVG_CHARACTER_WEAPONS)
    for row in cur:
        print('\033[36mAverage Character Weapons:\033[00m', row[0])

    con.close()

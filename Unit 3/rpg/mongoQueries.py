"""Queries for reading data from MongoDB

Robert Davis
2021/09/09"""


import pymongo
import sys


def mongo_connect(
    password,
    user='RCD2021',
    dbname='myFirstDatabase'
):
    """Connects to the MongoDB. Pass through the password,
returns the db."""

    client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}\
@cluster0.z3tac.mongodb.net/{dbname}?retryWrites=true&w=majority")
    db = client.test

    return db


if __name__ == '__main__':
    db = mongo_connect(sys.argv[1])

    print('\033[31mIt just won\'t work, life is hopeless')
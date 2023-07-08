#!/usr/bin/env python3

"""
Write a Python script that provides some stats
about Nginx logs stored in MongoDB:
Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method =
["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
(see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
"""


from pymongo import MongoClient


def loggedStats():
    """logs the stats"""
    client = MongoClient()
    db = client.logs
    coll = db.nginx
    print("{} logs".format(coll.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"\tmethod {method}: " +
              f"{coll.count_documents({'method': method})}")
    print(f"{coll.count_documents({'method': 'GET', 'path': '/status'})} \
status check")


if __name__ == "__main__":
    loggedStats()

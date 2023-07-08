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


import pymongo


def log_stats():
    """ provides some nginx stats """
    client = pymongo.MongoClient()
    db = client.logs
    logs = db.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    status = logs.count_documents({'method': 'GET', 'path': '/status'})
    # print the number of logs
    print(f"{logs.count_documents({})} logs")
    # print the number of methods
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {logs.count_documents({'method': method})}")
    # print status check
    print(f"{status} status check")


if __name__ == "__main__":
    log_stats()

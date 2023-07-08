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


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Affiche les statistiques des logs Nginx à partir d'une collection MongoDB.

    Args:
        mongo_collection (pymongo.collection.Collection): La collection MongoDB
          contenant les logs Nginx.
        option (str, optional): Option pour filtrer
          les statistiques par méthode.
          Par défaut, toutes les statistiques sont affichées.

    Returns:
        None

    """
    if option:
        query = {"method": option}
        count = mongo_collection.count_documents(query)
        print(f"method {option}: {count}")
    else:
        total_logs = mongo_collection.count_documents({})
        print(f"{total_logs} logs")
        print("Methods:")
        for method in METHODS:
            count = mongo_collection.count_documents({"method": method})
            print(f"\tmethod {method}: {count}")
        status_check_count = mongo_collection.count_documents(
                                                              {"method":
                                                               "GET",
                                                               "path":
                                                               "/status"
                                                               }
                                                              )
        print(f"{status_check_count} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    log_stats(collection)

#!/usr/bin/env python3
"""
A module of python script to provide stats about nginx
"""


def log_stats(mongo_collection):
    """
    Provides stats about Nginx logs stored in MongoDB.

    Args:
        mongo_collection: pymongo collection object for the Nginx logs.

    Output:
        Prints stats about the logs in the collection.
    """
    total_logs = mongo_collection.count_documents({})
    print("{} logs".format(total_logs))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    status_check_count = mongo_collection.count_documents(
            {"method": "GET", "path": "/status"})
    print("{} status check".format(status_check_count))

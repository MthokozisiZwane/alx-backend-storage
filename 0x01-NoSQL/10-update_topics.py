#!/usr/bin/env python3
"""
Module containing function to changes topics of school collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the school name.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

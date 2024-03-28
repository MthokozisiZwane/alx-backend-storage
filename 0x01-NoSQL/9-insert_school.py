#!/usr/bin/env python3
"""
Module containing function to insert a new document
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on keyword arguments
    """
    return mongo_collection.insert_one(kwargs).inserted_id

#!/usr/bin/env python3
"""
Module with python function to return students sorted by average
"""


def top_students(mongo_collection):
    """
    that returns all students sorted by average score
    """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {"_id": "$_id", "averageScore":
                    {"$avg": "$topics.score"}, "name": {"$first": "$name"}}},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))

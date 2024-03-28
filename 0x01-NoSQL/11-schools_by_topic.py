#!/usr/bin/env python3
"""
A module with function to get schools with a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieves the list of schools having a specific topic.
    """
    return list(mongo_collection.find({"topics": topic}))

#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document based on keyword arguments
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id

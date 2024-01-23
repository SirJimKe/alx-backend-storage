#!/usr/bin/env python3
"""Update topics"""


def update_topics(mongo_collection, name, topics):
    """
    updates the topics of a school document based on the name
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics }}
    )

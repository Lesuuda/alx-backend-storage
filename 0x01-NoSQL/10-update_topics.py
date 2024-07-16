#!/usr/bin/env python3
"""
changes school topics
"""


def update_topics(mongo_collection, name, topics):
    """changes school topics"""
    mongo_collection.update_many(
            {'name': name},
            { '$set': {'topics': topics} }
)

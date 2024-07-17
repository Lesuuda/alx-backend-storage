#!/usr/bin/env python3
"""inserts a document to a collection"""


def insert_school(mongo_collection, **kwargs):
    """inserts a document to a colection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id


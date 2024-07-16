#!/usr/bin/env python3
"""
lists all documents in a colection
"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    doc_list = [doc for docs in mongo_collection.find()]
    if len(doc_list) < 1:
        return []
    return doc_list


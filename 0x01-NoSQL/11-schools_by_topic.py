#!/usr/bin/env python3
"""returns list of school having a specific topic"""



def schools_by_topic(mongo_collection, topic):
    """returns a list of schools havin a specific topuc"""
    topic_filter = {
            'topics': {
                '$elemMatch': {
                    '$eq': topic,
                    },
                },
            }
    return [doc for doc in mongo_collection.find(topic_filter)]


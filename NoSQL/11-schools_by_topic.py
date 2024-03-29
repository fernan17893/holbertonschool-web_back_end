#!/usr/bin/env python3
""" 11-main """

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    if mongo_collection is None:
        return None
    return mongo_collection.find({"topics": topic})

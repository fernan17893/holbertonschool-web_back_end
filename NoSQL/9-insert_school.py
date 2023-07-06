#!/usr/bin/env python3
""" 9-main """

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """
    if mongo_collection is None:
        return None
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id

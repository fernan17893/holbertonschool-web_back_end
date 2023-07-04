#!/usr/bin/env python3
""" 8-main """

from pymongo import MongoClient



def list_all(mongo_collection):
    """ lists all documents in a collection """
    if mongo_collection is None or mongo_collection.find() is None:
        return []
    return mongo_collection.find()

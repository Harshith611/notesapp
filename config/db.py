from pymongo import MongoClient
# Example db.py file
# Use the service name defined in docker-compose.yml as the host
mongo_host = "mongodb"
mongo_port = 27017

conn = MongoClient(f"mongodb://{mongo_host}:{mongo_port}/")

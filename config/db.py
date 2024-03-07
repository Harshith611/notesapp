from pymongo import MongoClient
# Example db.py file
# Use the service name defined in docker-compose.yml as the host
mongo_uri="mongodb+srv://harshithkumar6510:harshithkumar6510@cluster0.uomdcii.mongodb.net/"
conn=MongoClient(mongo_uri)

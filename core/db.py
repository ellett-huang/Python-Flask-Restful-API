from pymongo import MongoClient
import config 

global mongodb 
client = MongoClient(config.mongodbConfig)
mongodb=client.Talett


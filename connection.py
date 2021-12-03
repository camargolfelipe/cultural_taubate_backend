import pymongo
from pymongo import MongoClient


DataBase = MongoClient('localhost', 27017)
# Criar a conexao com o Mongo
db = DataBase['tvtaubate']

collection = db['usuarios']
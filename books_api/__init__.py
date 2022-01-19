from flask import Flask
from pymongo import MongoClient
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

# Connecting to local host 
client = MongoClient('mongodb://localhost:27017/')

# Get the books_db and store in db
db = client.books_db

from .books import Books

api.add_resource(Books, '/books')
from flask_restful import Resource, reqparse
from . import db
from bson import json_util
import json

books_data = reqparse.RequestParser()
books_data.add_argument('page', type=int, required=True, help='Page number is required!')
books_data.add_argument('limit', type=int, required=True, help='Page Limit is required!')


class Books(Resource):
    '''
        Methods related to the Books endpoint is written here.

        GET:
            Input: {'page':Int, 'limit':Int}
            Output: {'total_number':Int, 'page':Int, 'showing':Int, books:List}
    '''

    def get(self):
        data = books_data.parse_args()

        page = data['page']
        page_limit = data['limit']

        # Insert books on try
        # db.books.insert_many([{'title':'Solomon'},{'title':'Mary'},{'title':'John'},{'title':'Susan'},{'title':'Tim'},{'title':'Alex'},{'title':'Tony'},{'title':'Michael'},{'title':'Snow'},{'title':'Samson'},{'title':'Jude'}])

        # Total number of books
        books_count = db.books.count_documents({})

        # Fetching books data and paginating
        fetch_books = db.books.find().sort('_id', -1).skip(page_limit * (page - 1)).limit(page_limit)

        books_fetched = list(json.loads(json_util.dumps(fetch_books)))

        response = {'total_number': books_count, 'page': page, 'showing': page_limit, 'books': books_fetched}

        return response
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)


CORS(app)

app.config['DEBUG'] = True

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'orders_details',
    'host': 'localhost',
    'port': '5432',
}

MONGO_DBNAME = 'Customers'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['MONGO_URI'] = 'mongodb://localhost:27017/%s' % MONGO_DBNAME


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mongo = PyMongo(app)
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run()

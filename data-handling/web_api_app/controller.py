from flask import jsonify
from base import app, mongo
from models import *


@app.route('/')
def main():
    return 'Welcone to Orders API!'

# Fetch data from the PosgreSQL Database and serve on the flask API


@app.route("/deliveries", methods=['GET'])
def get_deliveries():
    try:
        deliveries = Deliveries.query.all()
        return jsonify([e.serialize() for e in deliveries])
    except Exception as e:
        return(str(e))


@app.route("/order_items", methods=['GET'])
def get_order_items():
    try:
        order_items = Order_items.query.all()
        return jsonify([e.serialize() for e in order_items])
    except Exception as e:
        return(str(e))


@app.route("/orders", methods=['GET'])
def get_orders():
    try:
        orders = Orders.query.all()
        # List Ids
        customers = get_customers_model()
        result = []
        for order in orders:
            for customer in customers:
                if customer["user_id"] == order.customer_id:
                    result.append(order.serialize(customer))
        return jsonify(result)
    except Exception as e:
        return(str(e))


@ app.route("/orders/<id_>", methods=['GET'])
def get_by_id(id_):
    try:
        order = Orders.query.filter_by(id=id_).first()
        cus_id = order.customer_id
        cus_field = mongo.db.customers.find_one({"user_id": cus_id})
        customer = {
            'name': cus_field['name'],
            'user_id': cus_field['user_id'],
            'company_id': cus_field['company_id']
        }
        return jsonify(order.serialize(customer))
    except Exception as e:
        return(str(e))

# Fetch data from the MongoDB database and serve on the flask API


@ app.route('/customers', methods=['GET'])
def get_all_customers():
    try:
        customers = mongo.db.customers
        result = []
        for field in customers.find():
            result.append({'_id': str(field['_id']),
                           'name': field['name'],
                           'user_id': field['user_id'],
                           'company_id': field['company_id']})
        return jsonify(result)
    except Exception as e:
        return(str(e))


@ app.route('/companies', methods=['GET'])
def get_all_companies():
    try:
        customers_companies = mongo.db.customers_companies
        result = []
        for field in customers_companies.find():
            result.append({'_company_id': field['company_id'],
                           'company_name': field['company_name']})
        return jsonify(result)
    except Exception as e:
        return(str(e))

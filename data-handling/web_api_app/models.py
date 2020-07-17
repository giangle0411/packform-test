from base import db, mongo


class Deliveries(db.Model):
    __tablename__ = 'deliveries'

    id = db.Column(db.Integer, primary_key=True)
    order_item_id = db.Column(db.Integer, db.ForeignKey('order_items.id'))
    delivered_quantity = db.Column(db.Integer)

    def __init__(self, order_item_id, delivered_quantity):
        self.order_item_id = order_item_id
        self.delivered_quantity = delivered_quantity

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'order_item_id': self.order_item_id,
            'delivered_quantity': self.delivered_quantity,
        }


class Order_items(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    price_per_unit = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    product = db.Column(db.String())
    deliveries = db.relationship("Deliveries")

    def __init__(self, order_id, price_per_unit, quantity, product):
        self.order_id = order_id
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.product = product

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'price_per_unit': self.price_per_unit,
            'quantity': self.quantity,
            'product': self.product,
            'deliveries': [delivery.serialize() for delivery in self.deliveries]
        }


class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date)
    order_name = db.Column(db.String())
    customer_id = db.Column(db.String())
    order_items = db.relationship("Order_items")

    def __init__(self, created_at, order_name, customer_id):
        self.created_at = created_at
        self.order_name = order_name
        self.customer_id = customer_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self, customer={}):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'order_name': self.order_name,
            'customer_id': self.customer_id,
            'order_items': [order_item.serialize() for order_item in self.order_items],
            'customer': customer
        }


def get_customers_model():
    orders = Orders.query.all()

    cus_ids = [order.customer_id for order in orders]

    customers_raw = mongo.db.customers.find(
        {"user_id": {"$in": cus_ids}})

    customers = [{
        'name': customer['name'],
        'user_id': customer['user_id'],
        'company_id': customer['company_id'],
    } for customer in customers_raw]

    cus_company_ids = [customer['company_id'] for customer in customers]

    cus_company_raw = mongo.db.customers_companies.find(
        {"company_id": {"$in": cus_company_ids}})

    companies = [{
        'company_id': company['company_id'],
        'company_name': company['company_name']
    } for company in cus_company_raw]

    for customer in customers:
        for company in companies:
            if customer['company_id'] == company['company_id']:
                customer['company'] = company
    return customers

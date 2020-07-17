from pymongo import MongoClient
import pandas as pd

# Write .csv file data into MongoDB


class MongoDB(object):

    def __init__(self, dBName=None, collectionName=None):
        self.dBName = dBName
        self.collectionName = collectionName

        self.client = MongoClient("localhost", 27017)

        self.DB = self.client[self.dBName]
        self.collection = self.DB[self.collectionName]

    def InsertData(self, path=None):
        df = pd.read_csv(path)
        data = df.to_dict('records')

        self.collection.insert_many(data, ordered=False)
        print("All the Data has been Exported to MongoDB Server")


if __name__ == "__main__":
    mongodbCustomer = MongoDB(dBName='Customers', collectionName='customers')
    mongodbCustomerCompanies = MongoDB(
        dBName='Customers', collectionName='customers_companies')
    mongodbCustomer.InsertData(
        path="..\database\Test task - Mongo - customers.csv")
    mongodbCustomerCompanies.InsertData(
        path="..\database\Test task - Mongo - customer_companies.csv")

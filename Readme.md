# Giang's Packform intern test

## Back-end

The project backend solution is located in '/data-handling' directory.

```
cd /data-handling
```

### Write .csv file to databases

```
cd data_migration_app
```

#### Write respective .csv files to MongoDB database

Enter the following command to initialise the MongoDB database and write .csv file data

```
py insert_mongodb_data.py
```

#### Write respective .csv files to postgreSQL database

1. Create a new postgreSQL database to save our collections by running the following command

```
py create_postgre_db.py
```

2. After creating postgreSQL database, .csv file data can be written into the database

```
py insert_postgresql_data.py
```

### Serve the database APIs

The project's backend runs on a Python 3 virtual environment. To install virtual environment, enter the following command:

```
cd /web_api_app
pipenv install
pipenv shell
```

Then the APIs can be served from a Python Flask Application

```
py manage.py runserver
```

The API will be served on default localhost port 5000 (localhost:5000)

## Front-end

The Vue.js Application is stored in display-data directory

```
cd /display-data
```

To run the Vue.js Application and display the data from the database, run the following commands:

```
npm install
npm run serve
```

The Application will be served on default localhost port 8080 (localhost:8080)

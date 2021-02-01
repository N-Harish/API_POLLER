import pymongo


def db() -> pymongo.database.Database:
    client = pymongo.MongoClient('mongodb+srv://<username>:<password>@cluster0.jmjw9.mongodb.net/<dbname>?retryWrites=true&w=majority')
    dbs = client.get_database('API_POLLER')
    return dbs


def get_db_api1() -> pymongo.collection.Collection:
    dba = db()
    api1_ref = dba.get_collection('API_POLL_DB')
    # api1_ref.insert_one(data)
    return api1_ref


def get_db_api2() -> pymongo.collection.Collection:
    dba = db()
    api2_ref = dba.get_collection('API_POLL_DB2')
    # api1_ref.insert_one(data)
    return api2_ref

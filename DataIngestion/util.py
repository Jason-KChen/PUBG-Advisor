# from dotenv import load_dotenv
# load_dotenv()

# from dbConfig import MONGODB_CONFIG
# from data_migration_pipelines.base_data_migration_pipeline import (
#     BaseDataMigrationPipeline
# )
from pymongo import UpdateOne, MongoClient

from pprint import pprint
from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne, WriteConcern
from pymongo.errors import BulkWriteError



# match_connection = MongoClient(**MONGODB_CONFIG)
# match_collection = match_connection[]

client = MongoClient('localhost', 27017)
# os.getenv("MONGODB_CONFIG")

teleArr = []

db = client.test_database
collection = db.test_collection

coll = db.get_collection(
    'test', write_concern=WriteConcern(w=3, wtimeout=1))

def writeToMongo(arr):
    if len(arr) > 0:
        try:
            
            db.test_collection.bulk_write([
                # InsertOne({'_id':teleArr[2]}),
                InsertOne({
                    'telemetricURL': arr[i][0],
                    'gameCreationTime': arr[i][1],
                    'mapName': arr[i][2]}) for i in range(len(arr))
                ])
        except BulkWriteError as bwe:
            pprint(bwe.details)
    # logger.info(f'Loaded {} matches into db')

# if __name__ == "__main__":
#     file = open('./data_partitions/filtered_match_ids_partition_1.txt', 'r')
#     print(file.readline())
#     for line in file:
        
#         sline = line.split(',')
#         teleArr.append(sline)

#     file.close()
#     writeToMongo(teleArr)
    # print(teleArr)
    # db.test_collection.drop()

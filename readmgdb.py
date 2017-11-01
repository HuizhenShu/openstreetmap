from datetime import datetime
mapping = {
            '201315 上海':'201315', 
            '2000080':'200080', 
            '21500':'215027', 
            '21351':'213353', 
            }

def range_query():
    # Modify the below line with your query.
    # You can use datetime(year, month, day) to specify date in the query
    #query = {'created.timestamp':{'$gt':"2017-01-01"}}
    #query = {"amenity": "restaurant"}
    #query = {"address.postcode": "21351"}
    query = {"address.street": "竹箦镇"}
    return query

# Do not edit code below this line in the online code editor.
# Code here is for local use on your own computer.
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.osmfinal
    return db
def aggregate(db, pipeline):
    return [doc for doc in db.autos.aggregate(pipeline)]#

if __name__ == "__main__":
    # For local use
    db = get_db()
    for i in range(len(mapping)):
        db.autos.update({'address.postcode':list(mapping.keys())[i]},{"$set":{' address.postcode ':list(mapping.values())[i]}},multi=True)
    # query = range_query()
    # autos = db.autos.find(query)


    # print(autos.count())
    # for i in autos:
    #     print(i)
    # pipeline = [{"$match":{"amenity": "restaurant"}},
    # {"$group":{"_id":"$address.street","count":{"$sum":1}}},
    # {"$sort":{"count":-1}}
    # ,{"$limit":5}]
#     pipeline = [#{"$match":{"amenity": "restaurant"}},
#     {"$group":{"_id":"$address.postcode","count":{"$sum":1}}},
#     {"$sort":{"count":-1}}
#     ]#,{"$limit":5}
#     result = aggregate(db, pipeline)
#     for i in range(len(result)):
#         if result[i]['_id']:
#             print(result[i],len(result[i]['_id']))
#     print(result)
#     print(len(result))

# {'_id': '201315 上海', 'count': 2} 9
# {'_id': '2000080', 'count': 2} 7
# {'_id': '21500', 'count': 2} 5
# {'_id': '21351', 'count': 1} 5




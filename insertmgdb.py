#!/usr/bin/env python
""" 
Add a single line of code to the insert_autos function that will insert the
automobile data into the 'autos' collection. The data variable that is
returned from the process_file function is a list of dictionaries, as in the
example in the previous video.
"""
import json
def load(file):
    with open(file) as json_file:
        data = json.load(json_file)
        print (len(data))
        return data

# def process_file(infile):

# load('sample.osm.json')

def insert_autos(infile, db):
    data = load(infile)
    # Add your code here. Insert the data in one command.
    for i in range(len(data)):
    	db.autos.insert(data[i])
  
if __name__ == "__main__":
    # Code here is for local use on your own computer.
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.osmfinal

    insert_autos('shanghai_china.osm.json', db)
    # print db.autos.find_one()
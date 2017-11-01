#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
"""

"""
# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017")
# db = client.osm
# myset = db.osmset
def floatornot(aa):
	try:
	    aa = float(aa)
	    return True
	except ValueError:
	    print ("not a number")
	    return False

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]
result = []
def shape_element(element):
    node = {}
    taglist1 = ["id","type","visible"]
    taglist2 = ["changeset","timestamp","user","uid"]
    taglist3 = ["lat","lon"]
    if element.tag == "node" or element.tag == "way" :
        # YOUR CODE HERE
        #print element.attrib
        
       
        created = {}
        pos = []
        for i in range(len(taglist1)):
            if taglist1[i] in element.attrib:
                node[taglist1[i]] =element.attrib[taglist1[i]]
        for i in range(len(taglist2)):
            if taglist2[i] in element.attrib:
                created[taglist2[i]] =element.attrib[taglist2[i]]     
        for i in range(len(taglist3)):
            if taglist3[i] in element.attrib:
                if floatornot(element.attrib[taglist3[i]]):
                    pos.append(element.attrib[taglist3[i]])          
        
        node["created"] = created
        node["pos"] = pos
        address = {}
        for tag in element.iter("tag"):
            ptag = problemchars.search(tag.attrib['k'])
            #print ptag
            splitk = tag.attrib['k'].split(':')
            if len(splitk)==1 :#problem have not been used
                node[splitk[0]]=tag.attrib['v']
            if 'addr' in tag.attrib['k'] and len(splitk)==2:
                address[splitk[1]] = tag.attrib['v']#get the attr后de第一个参数，如果有两个以上的参数不成立
            
            #print address

            
            pass
        node_refs = []
        for nd in element.iter("nd"):
            node_refs.append(nd.attrib["ref"])
        node["type"] = element.tag
        node["node_refs"] = node_refs
        node["address"] = address
        result.append(node)
        #print (node)
        return node
    else:
        return None


def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    for _, element in ET.iterparse(file_in):
        el = shape_element(element)
        if el:
            data.append(el)
    with codecs.open(file_out, "w") as fo:
        fo.write("[")
        for i in range(len(data)-1):
            if pretty:
                fo.write(json.dumps(data[i], indent=2)+","+"\n")
            else:
                fo.write(json.dumps(data[i])+"," + "\n")
        if pretty:
            fo.write(json.dumps(data[len(data)-1], indent=2)+"\n")
        else:
            fo.write(json.dumps(data[len(data)-1]) + "\n")
        fo.write("]")
    return data

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the process_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
    data = process_map('shanghai_china.osm', pretty=False)
    #pprint.pprint(data[1:100])

if __name__ == "__main__":
    test()
    #print (result[1000]) load
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "sample.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = []

# UPDATE THIS VARIABLE
mapping = { 
            # "road": "路",
            # "Road":"路",
            "#1": "",
            "Lane 30 of West Dalian Road":"",
            "Lane 82 of East Yanji Road":"",
            "Xiuyan Road":"秀沿路",
            "Songhua Community":"",
            "yindu road":"银都路",
            "Jiashan Market":"嘉善老市"
            }

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

    print (street_types)
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
   # osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osmfile):#, events=("start",)

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    #osm_file.close()
    return street_types


def update_name(name, mapping):
   # print type(name)
    # YOUR CODE HERE
    for i in range(len(mapping.keys())):
        #print type(mapping.keys()[i]),mapping.values()[i]
        name = name.replace(list(mapping.keys())[i],list(mapping.values())[i])
        #name = name.replace("Streetreet","Street")
    #print (name)
    return name


def test():
    st_types = audit(OSMFILE)
    print(st_types)
    # assert len(st_types) == 3
    # #pprint.pprint(dict(st_types))

    for st_type, ways in st_types.items():
        for name in ways:
            print(name)
            better_name = update_name(name, mapping)
            print (better_name)
    #         #print name, "=>", better_name
    #         if name == "West Lexington St.":
    #             assert better_name == "West Lexington Street"
    #         if name == "Baldwin Rd.":
    #             assert better_name == "Baldwin Road"


if __name__ == '__main__':
    test()
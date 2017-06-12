import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

osm_file = open("E:\Projects\Python\Intro DataScience\data\south_carolina.osm","r", encoding='utf-8')

street_type_re = re.compile(r'\b\S+\.?$',re.IGNORECASE)
postcode_type_re = re.compile(r'29([0-9]).+',re.IGNORECASE)
lower = re.compile(r'^([a-z]|_)*$') #zipcod that starts with 29
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
street_types = defaultdict(set)
postalCode_types = defaultdict(set)

#define expected values
expected = ["Street","Avenue","Boulevard","Drive","Court","Place","Lane","Circle","Road"]
expected_postalCodes = ["29016"]

mapping = { "St": "Street",
            "St.": "Street",
            "Ave" : "Avenue",
            "Ave." : "Avenue",
            "RD" : "Road",
            "Rd" : "Road",
            "Blvd" : "Boulevard",
            "D" : "Drive"
            }


def audit_steet_type(steet_types,street_name):
    m = street_type_re.search(street_name)
    if m:
        steet_type = m.group()
        if steet_type not in expected:
            steet_types[steet_type].add(steet_type)


def audit_postcode_type(postalCode_types,postalCode):
    m = postcode_type_re.search(postalCode)
    if m:
        postal_types = m.group()
        if postalCode not in expected_postalCodes:
            postalCode_types[postal_types].add(postal_types)

#truncate everything past 5 chars for zipcode
def audit_postalcode_scrub_zip():
    for i in postalCode_types.keys():
        if i.__len__() > 5:
            postalCode_types[i] = i[:5] #substring of first 5 char

#check the value of the attribute of a tag
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def is_postal_code(elem):
    return (elem.attrib['k'] == "addr:postcode")

def auditSteetNames():
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "way": #linear feature (road, rivers, roads, highways
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                     audit_steet_type(street_types,tag.attrib['v'])

def auditPostalCodes():
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "way": #linear feature (road, rivers, roads, highways
            for tag in elem.iter("tag"):
                if is_postal_code(tag):
                    audit_postcode_type(postalCode_types,tag.attrib['v'])


if __name__ == '__main__':
    #auditSteetNames()
    auditPostalCodes()
    audit_postalcode_scrub_zip()
    pprint.pprint(dict(postalCode_types))
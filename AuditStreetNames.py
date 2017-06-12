import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

osm_file = open("E:\Projects\Python\Intro DataScience\data\south_carolina.osm","r", encoding='utf-8')

street_type_re = re.compile(r'\b\S+\.?$',re.IGNORECASE)
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

street_types = defaultdict(set)

#define expected values
expected = ["Street","Avenue","Boulevard","Drive","Court","Place","Lane","Circle"]
search_cuisine_category = ["breakfast"]

def audit_steet_type(steet_types,street_name):
    m = street_type_re.search(street_name)
    if m:
        steet_type = m.group()
        if steet_type not in expected:
            steet_types[steet_type].add(steet_type)

#check the value of the attribute of a tag
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def audit():
    #itparse parses one line at a time, starting with start tag (top level)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                     audit_steet_type(street_types,tag.attrib['v'])
    pprint.pprint(dict(street_types))

if __name__ == '__main__':
    audit()
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
import AuditWays as w
import pprint
import pandas as pd
'''
    This is the main driver py file. 
'''

osm_file = open("E:\Projects\Python\Intro DataScience\data\south_carolina.osm","r", encoding='utf-8')
wayDic = {}

def auditWayTags():
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "way": #linear feature (road, rivers, roads, highways
            way = w.Way() #create new way object
            way.__setId__(elem.attrib['id'])
            way.__setTimeSpamp__(elem.attrib['timestamp'])
            way.__setUID__(elem.attrib['uid'])
            way.__setChangeSet__(elem.attrib['changeset'])

            for tag in elem.iter("tag"):
                way.__setTagTags__(tag.attrib['k'],tag.attrib['v'])

            for tag in elem.iter("nd"):
                way.__setNDtag__(tag)

            wayDic.__setitem__(way.__getId__(),way.__getTagTags__())

auditWayTags()
wayDf = pd.DataFrame.from_dict(wayDic,'index')
pprint.pprint(wayDf)
wayDf.to_csv('C:\\Users\Travis\Desktop\output.csv')


import xml.etree.ElementTree as et
import pprint

tree = et.parse('E:\Projects\Python\Intro DataScience\data\south_carolina.osm')
root = tree.getroot()

print("\nChildren of root : ")
for child in root:
    print (child.tag)



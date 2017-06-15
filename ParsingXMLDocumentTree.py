import xml.etree.ElementTree as et
import pprint

tree = et.parse('E:\Projects\Python\Intro DataScience\data\south_carolina.osm')
root = tree.getroot()

#print the tag attribute of each child element.
#print("\nChildren of root : ")
#for child in root:
#    print (child.tag)

#xpath
highway = root.find('./way/tag')
highway_name = ""
for h in highway:
    highway_name += h
print ("\n highway name: \n", highway_name)

def is_street_name(elem):
    return (elem.attrib['v'] == "Starbucks")

for a in root.findall('./way'):
    print(is_street_name)


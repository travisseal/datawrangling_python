'''
    This script will model the data elements of the Ways elements in the dataset.
'''

class Way:

    def __init__(self):
        #print('way created')
        self.ndTags = []
        self.TagTags = {}

    def __setId__(self,id):
        self.id = id;

    def __setTimeSpamp__(self,timestamp):
        self.timeStamp = timestamp

    def __setChangeSet__(self,changeSet):
        self.changeSet = changeSet

    def __setUID__(self,uid):
        self.uid = uid

    def __setNDtag__(self,ndtag):
        self.ndTags.append(ndtag)

    def __setTagTags__(self,key,value):
        self.TagTags.__setitem__(key,value)

    def __getId__(self):
        return self.id

    def __getTimeStamp__(self):
        return self.timeStamp

    def __getTagTags__(self):
        return (self.TagTags)

import thefuzz
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
ddddbbbb = client['ICODEX-GOLDENDB']
collection = ddddbbbb['journal']

class similaritycheck:   # to compare sliced input reference and the existing documents in the goldendatabase
    def __init__(self,dict1):    #doi1 = first we compare doi , if doi = "" ,then we compare the whole values
        self.dict1 = (dict1)


    def doiquest(self):
        doi = self.dict1.get('doi')
        if doi != "":
            query = collection.find({'doi':str(doi)})
            for i in query:
                return i

            else:
                return 0

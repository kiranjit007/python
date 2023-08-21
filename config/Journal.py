import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["iRef_Data1"]
collection_name = mydb["Journal"]

db01 = client['ICODEX-DB01']
col01j = db01['Journal']
col01b = db01['Book']


db1 = client['iRefDb0']
col1 = db1['refstrings']

db2 = client['ICODEX']
col02j = db2['journal']
col02b = db2['book']

dbg = client['ICODEX-GOLDENDB']
colgj = dbg['journal']
colgb = dbg['book']
#list = {'_id': 'bib1', 'refstring': 'Rodrik, D., (1991). Policy uncertainty and private investment in developing countries. Journal of Development Economics, volume 36, pages 229–242.', 'status': 'Incomplete'}

#col1.insert_one(list)
# for i in col1.find():
#     print(i)
#     filter = {'ReferenceString':'Anand is a guy, and still not an author, what a pity'}
#     newvalues = {"$set": {'status3': 'Incomplete'}}
#     col1.update_one(filter, newvalues)


dict1 = {

  "type": "Journal",
  "authors": [
    {
      "lastname": "Becker",
      "firstname": "KD"
    },
    {
      "lastname": "Bradshaw",
      "firstname": "CP"
    },
    {
      "lastname": "Domitrovich",
      "firstname": "C"
    },
    {
      "lastname": "Ialongo",
      "firstname": "NS"
    }
  ],
  "groups": [
    {
      "groupname": "Research Group"
    },
    {
      "groupname": "The Metropolitan Area Child Study Research Group"
    }
  ],
  "firstPage": "482",
  "lastPage": "493",
  "issue": "6",
  "journalTitle": "Administration and policy in mental health",
  "articleTitle": "Coaching teachers to improve implementation of the good behavior game.",
  "url": "10.1007/s10488-013-0482-8",
  "volume": "40",
  "year": "2013"
}

#colgj.insert_one(dict1)



















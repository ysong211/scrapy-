from pymongo import MongoClient
import urllib.request as urllib2


# ???????
conn = MongoClient('localhost',27017)
# db = conn.jdgoods

db = conn['jdgoods']

# ??????
# myset = db.name
coll = db['name']
cusor = coll.find({},{'good_url':1,'_id':0})


goodurls = []
for v in cusor:
    a = v['good_url']
    goodurls.append(a)
    # print(goodurls)


for i in goodurls:
    request = urllib2.Request(i)
    response = urllib2.urlopen(request)
    buff = response.read()
    html = buff.decode()
    print(html)





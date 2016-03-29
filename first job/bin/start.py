import string
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import cPickle
import comp
co=comp.Comp()
co.creatWord()
client = MongoClient('localhost',27017)
db = client.hinews
datas = db.article.find()
#print  len(datas)
i=1
for data in datas:
	try:
		vector=cPickle.loads(data['feature'])
		matrx=vector.toarray()[0]
		categorys=data['category']
		for category in categorys:
			co.update(category,matrx)
	except:
		co.writeFile()
		print "Exception Error:%d"%(i)
	if i%100==0:
		print "Completed %d......"%(i)
	if i%10000==0:
		co.writeFile()
		print "Completed write :%d"%(i)
	i=i+1
co.writeFile()
print "over......"

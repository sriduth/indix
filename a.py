from collections import defaultdict
import sys
import os
import hashlib

DATA = []
HISTORY = {}
word_frequency = {}
words = []

def search(querystring):
	#create digestor >_>

	querystring = querystring.split("/")
	md = hashlib.md5()
	md.update(str(querystring))
	query_hash = md.hexdigest()

	for key,obj in HISTORY.iteritems():
		if key == query_hash:
			obj.get_results()
			return 

	queries = []
	results = defaultdict(int)

	for query in querystring: 
		if query[len(query)-1] == 's':
			queries.append(query[:-1])
		else:
			queries.append(query)

	for prod in DATA:
		data = prod.has_key(queries)
		if len(data) != 0:
			results[str(data)+" : "+str(prod.data())] = len(data)

	sorted(results.iteritems(),key=results.get,reverse=True)

	#md.update(str(querystring))
	HISTORY[md.hexdigest()] = History(results,md.hexdigest())

	for k,v in  results.iteritems():  
	 	print "Matched %s words : \n%s\n" % (str(v), str(k))

	print "Total Items found : ",len(results)

class Product:

	keywords = []
	product_description = ""

	def __init__(self,product_des):
		self.product_description = product_des
		self.keywords = product_des.split(" ")

	def has_key(self,queries):
		result = []
		for key in queries:
			if key in self.keywords:
				result.append(key)

		return result

	def data(self):
		return self.product_description

class History:

	results = defaultdict(int)
	search_keys = []
	def __init__(self,results,search_keywords,):
		self.results = results
		self.search_keys = search_keywords

	def get_hash(self):
		return self.search_keys

	def get_results(self):
		print "here"
		for k,v in  self.results.iteritems():  
	 		print "Matched %s words : \n%s\n" % (str(v), str(k))

	 	print "Total Items found in History: ",len(self.results)


#<----------------------------------------------------------------preprocessing
input_file =open("i.txt","r")
file_data = input_file.read()

products = file_data.split("\n")
#<----------------------------------------------------------------preprocessing

# create and define "Product"
for prod in products:
	DATA.append(Product(prod.lower()))

while True :
	query = raw_input("Enter a query?\nFormat : <query>/<query>....")
	search(query.lower())

	# for key,obj in HISTORY.iteritems():
	# 	print obj

from app import app 
from flask import render_template 
import re
from elasticsearch import Elasticsearch


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index') 

def index():
    es = Elasticsearch(['192.168.158.74:9200']) 
    search_index="suricataids-bd-alert-2018.01.19"
    res = es.search(index=search_index, body={"query": {"match_all": {}}}, size=100)
    signatures=[]
    all_hits = res['hits']['hits']
    total = len(all_hits)
    for hit in all_hits:
	alert_obj = hit['_source']['alert']
	#print("Signature = %s"% alert_obj['signature'])
	if alert_obj['signature'] not in signatures:
	    signatures.append(alert_obj['signature'])
    return render_template('index.html', methods = ['GET', 'POST'], **locals())

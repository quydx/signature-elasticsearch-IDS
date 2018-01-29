from app import app 
import flask
from flask import render_template 
import re
from elasticsearch import Elasticsearch
from datetime import datetime
from app.form import SignatureForm


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index') 

def index():
    es = Elasticsearch(['192.168.158.74:9200']) 
    search_index="suricataids-bd-alert-" + datetime.now().strftime('%Y.%m.%d')
    res = es.search(index=search_index,
	    body={
		'query': {
		    'match_all': {}
		},
		'sort': [
		    {'timestamp': {'order': 'desc'}}   
		]
	    },
	    size=500
	    )
    signatures=[]
    all_hits = res['hits']['hits']
    total = len(all_hits)
    for hit in all_hits:
	alert_obj = hit['_source']['alert']
	if alert_obj['signature'] not in signatures:
	    signatures.append(alert_obj['signature'])

    cur_signs = []
    with open('app/all_signature') as f:
	for line in f:
	    cur_signs.append(line.rstrip('\n'))
     
    sfile = open('app/all_signature', 'a')
    for sig in signatures:
	if sig not in cur_signs:
	    sfile.write("%s\n" % sig)
    sfile.close()

    return render_template('index.html', methods = ['GET', 'POST'], **locals())

@app.route('/setting', methods=['GET','POST'])

def setting():
    form = SignatureForm()
    if flask.request.method == 'POST':
	signatures = flask.request.values.getlist('signatures[]')
	with open('app/signatures_warning', 'w') as f:
	    for sig in signatures:
		f.write("%s\n" % sig )
	f.close()
	
    else:
	cur_signatures = [ line.rstrip('\n') for line in open('app/signatures_warning')]
	all_signatures = []
	with open('app/all_signature') as f:
	    for line in f:
		all_signatures.append(line.rstrip('\n'))
    return render_template('setting.html', method = ['GET', 'POST'], **locals())




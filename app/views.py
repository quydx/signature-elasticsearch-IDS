from app import app 
import flask
from flask import render_template 
import re
from elasticsearch import Elasticsearch
from datetime import datetime
from app.form import *
from es_realtime_alert import *
import json



@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST']) 

def index():
    interval = 900
    severity = None
    query = ""
    body_sev = None
    body_non = None
    if flask.request.method == 'POST':
	interval = int(flask.request.values.get('time-query')) 
	severity = int(flask.request.values.get('severity-query'))

    form = TimeForm()
    es = Elasticsearch(['192.168.158.74:9200']) 
    search_index="suricataids-bd-alert-" + datetime.now().strftime('%Y.%m.%d')
    if severity:
	body_sev = {
	    "size":1000,
	    "query":{
		"bool": {
		    "must":[    
			{
			    "term":{
				"alert.severity": "%d"%severity    
			    }	
			},
			{
			    "range":{
				"timestamp":{
				    "gte":"now-%ds"%interval	
				}    
			    }
			}
		    ]	
		}   
	    }	    
	}
    else:
	body_non = {
	    "size":1000,
	    "query": {
		"range": {
		    "timestamp":{
			"gte":"now-%ds"%interval   
		    }	
		}   
	    },
	    "sort":[
		{"timestamp":{"order": "desc"}}    
	    ]
	}
    res = es.search(index=search_index,body = body_sev if severity else body_non)
    signatures=[]
    list_sig = []
    all_hits = res['hits']['hits']
    total = len(all_hits)
    for hit in all_hits:
	alert_obj = hit['_source']['alert']
	if alert_obj['signature'] not in list_sig:
	    list_sig.append(alert_obj['signature'])
	    signatures.append({'signature': alert_obj['signature'], 'severity':alert_obj['severity'], 'count':1})
	else:
	    for obj in signatures:
		if obj['signature'] == alert_obj['signature']:
		    obj['count'] +=1
		    break
		    


    cur_signs = []
    with open('app/all_signature') as f:
	for line in f:
	    cur_signs.append(line.rstrip('\n'))
     
    sfile = open('app/all_signature', 'a')
    for sig in signatures:
	if sig['signature'] not in cur_signs:
	    sfile.write("%s\n" % sig['signature'])
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




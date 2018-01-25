from datetime import datetime
from elasticsearch import Elasticsearch 
from pprint import pprint
import demo
import time

class ESAlert:
    def __init__(self, host, port):
	self.host = host
	self.port = port
	self.es = Elasticsearch([{'host': self.host, 'port' :self.port }])
    def query(self, index, body):
	try:
	   res = self.es.search(index=index, body=body)
	   return res
	except:
	    print "Search ERROR"
    def real_time_query(self, index, body):
	try:
	    while True:
		res = self.es.search(index=index, body=body)
		print("Find %d document ." % len(res['hits']['hits']) )
		time.sleep(28)
	except:
	    print("Realtime query except")

if __name__ == '__main__':
    e = ESAlert('192.168.158.74', 9200)
    body={
	"size":2,
	"query": {
	    "filtered": {
		"filter": {
		    "and": [
			{
			    "range": {
				"gt": "now-30s"    
			    }
			},
			{
			    "term": {
				"count": 1    
			    }	
			}
		    ]	
		}  
	    },
	},
	"sort":[
	    {"timestamp": {"order": "desc"}}
	]
    }
    query =  "alert.signature:\"GPL ICMP_INFO PING BSDtype\""
    body1= {
	"size":2,
	"query":{
	    "filtered":{
		"query":{
		    "query_string":{
			"query": "(ET SCAN Potential SSH Scan) OR (GPL RPC portmap listing UDP 111) OR (GPL ICMP_INFO PING BSDtype)",
			"fields": ["_all"]
		    }
		} 
	    },
#	    "query_string":{
#		"query": "(ET SCAN Potential SSH Scan) OR (GPL RPC portmap listing UDP 111) OR (GPL ICMP_INFO PING BSDtype)",
#		"fields": ["_all"]
#	    },
	    "filter":{
		"range":{
		    "timestamp":{
			"gte":"now-300s"    
		    }	
		}
	    }
	}
    }
    body2= {
	"size":1,
	"query": {
	    "bool":{
		"filter":{
		    "range":{
			"timestamp":{
			    "gte": "now-30s"	
			}    
		    }	
		},
		"must":{
		    "terms":{
			"alert.signature": ["\"ET SCAN Potential SSH Scan\"", "\"GPL RPC portmap listing UDP 111\"", "\"GPL ICMP_INFO PING BSDtype\""] 
			#"alert.signature" : "ET SCAN Potential SSH Scan"
		    }	
		}
	    }   
	} 	
    }
    e.real_time_query(
	index='suricataids-bd-alert-2018.01.25',
	body=body1
    )
    """
    signatures=[]
    all_hits = res['hits']['hits']
    time = res['took']
    print("Get res in %d ms" % time)
    print("Get total %d document from elasticsearch" % len(all_hits) )
    
    pprint(all_hits)
    
    for hit in all_hits:
	alert_obj = hit['_source']['alert']
	if alert_obj['signature'] not in signatures:
	    signatures.append(alert_obj['signature'])
    pprint(signatures)
    """



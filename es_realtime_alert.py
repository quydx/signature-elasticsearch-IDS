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

    def query(self, index, signature_list, interval):
	query = ""
	for signature in signature_list:
	    query += "(\"%s\")" % signature
	    query += " OR "
	query = query.rstrip(" OR ")
	
	body= {
	    "size":500,
	    "sort":[
		{
		    "timestamp":{
			"order": "desc",
			"unmapped_type": "boolean"
		    }	
		}  
	    ],
	    "query":{
		"filtered":{
		    "query":{
			"query_string":{
			    "query": query,
			}
		    },
		    "filter":{
			"bool":{
			    "must":[
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
	    }
	}
	#pprint(body)
	try:
	    res = self.es.search(index=index, body=body)
	    return res
	except:
	    print("Query Except ")

if __name__ == '__main__':
    e = ESAlert('192.168.158.74', 9200)
    query =  "alert.signature:\"GPL ICMP_INFO PING BSDtype\""
    #signature_list = ["ET SCAN Potential SSH Scan","GPL RPC portmap listing UDP 111","GPL ICMP_INFO PING BSDtype"]
    signature_list = [signature.rstrip("\n") for signature in open('app/signatures_warning')]
    res  = e.query(
	index='suricataids-bd-alert-2018.01.28',
	signature_list = signature_list
    )
    
    signatures=[]
    all_hits = res['hits']['hits']
    time = res['took']
    print("Get res in %d ms" % time)
    print("Get total %d document from elasticsearch" % len(all_hits) )
    
    pprint(all_hits)
    """
    for hit in all_hits:
	alert_obj = hit['_source']['alert']
	if alert_obj['signature'] not in signatures:
	    signatures.append(alert_obj['signature'])
    pprint(signatures)

    """





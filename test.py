from datetime import datetime
from elasticsearch import Elasticsearch 
from pprint import pprint

es = Elasticsearch(['192.168.158.74:9200'])
"""
res = es.search(index="suricataids-bd-alert-2018.01.19", body={"query": {"match_all": {}}}, size=10)
signatures=[]
all_hits = res['hits']['hits']
print("Get total %d document from elasticsearch" % len(all_hits) )

for hit in all_hits:
    alert_obj = hit['_source']['alert'])
    if alert_obj['signature'] not in signatures:
	signatures.append(alert_obj['signature'])
pprint(signatures)
"""
res = es.get_source(index='suricataids-bd-alert-2018.01.19' )
pprint(res[0])



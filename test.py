from datetime import datetime
from elasticsearch import Elasticsearch 
from pprint import pprint

es = Elasticsearch(['localhost:9200'])

res = es.search(index="suricata-bd-alert-*", body={"query": {"match_all": {}}} , filter_path=['hits.hits._index'])
print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])




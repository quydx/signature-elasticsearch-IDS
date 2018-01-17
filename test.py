from datetime import datetime
from elasticsearch import Elasticsearch 
from pprint import pprint

es = Elasticsearch(['localhost:9200'])

es.indices.create(index='test-index', ignore=400)
health = es.cluster.health(wait_for_status='yellow', request_timeout=1)
pprint(es.search(index='test-index', filter_path=['hits.hits._id', 'hits.hits._type']))
pprint(health)



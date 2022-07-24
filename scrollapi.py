'''
Elasticsearch scrollapi for fetching all logs above 10,000 threshold
'''
import json
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd

def parse_response(response):
    """
    Recieves a response from elasticsearch
    Returns scrollapi id and json response
    """
    try:
        res_json = response.json()
        data = res_json['hits']['hits']
        _scroll_id = res_json['_scroll_id']
    except KeyError:
        _scroll_id = None
        data = []
        print(str(response.json()))
    return res_json, data, _scroll_id

def get_all_logs(index_name):
    """
    Gathers and appends logs
    Returns a dataframe
    """
    elastic_url = \
    'https://cynergizer-ce1e21.es.us-central1.gcp.cloud.es.io:9243/'+index_name+'/_search?scroll=1m'
    scroll_api_url = 'https://cynergizer-ce1e21.es.us-central1.gcp.cloud.es.io:9243/_search/scroll'
    headers = {'Content-Type': 'application/json'}
    compiled = []
    temp = []

    payload = {
        "size": 100000,
        "query": { "match_all" : {}}
    }

    req_response = requests.request(
        "POST",
        elastic_url,
        data=json.dumps(payload),
        headers=headers,
        auth = HTTPBasicAuth('<elasticsearch_username>', '<elasticsearch_passcode>')
    )

    # fetching first batch data
    res_json, temp, _scroll_id = parse_response(req_response)
    compiled.extend(temp)
    # now fetching all logs with scroll id
    i = 1
    while temp:
        # scroll to get next batch data
        print("Fetching batch "+str(i))
        scroll_payload = json.dumps({
            'scroll': '1m',
            'scroll_id': _scroll_id
        })
        scroll_res = requests.request(
            "POST", scroll_api_url,
            data=scroll_payload,
            headers=headers,
            auth = HTTPBasicAuth('elastic', 'j1UnCKApb2N5VWU8wZmueUOK')
        )
        res_json, temp, _scroll_id = parse_response(scroll_res)
        compiled.extend(temp)
        i += 1
    return compiled

# example fetching data
web_df = get_all_logs('62558e285529969891a081a3`web_requests')
web_df = pd.DataFrame([x['_source'] for x in web_df])

ip_blocks = get_all_logs('ip-blocks')
ip_blocks = pd.DataFrame([x['_source'] for x in ip_blocks])

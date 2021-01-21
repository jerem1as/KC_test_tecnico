import requests
import json
import urllib

max_results = 500 
hapikey = '5adf730a-d272-470f-b6dc-29d96b510e0d' 
deal_list = []
get_all_leads_url = "https://api.hubapi.com/deals/v1/pipelines?"
parameter_dict = {'hapikey': hapikey}
headers = {}

parameters = urllib.parse.urlencode(parameter_dict)
get_url = get_all_leads_url + parameters
r = requests.get(url= get_url, headers = headers)
response_dict = json.loads(r.text)

for L in response_dict[0]["stages"]:
    for p in L:
        print (p+ ": " + str(L[p]))

    print ("-----------------")

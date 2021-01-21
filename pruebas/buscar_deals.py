import requests
import json
import urllib

max_results = 500 
hapikey = '5adf730a-d272-470f-b6dc-29d96b510e0d' 
get_all_deals_url = "https://api.hubapi.com/deals/v1/deal/paged?hapikey=" + hapikey

r = requests.get(url= get_all_deals_url)
response_dict = json.loads(r.text)

print (response_dict)


for deal in response_dict["deals"]:

    print (deal["dealId"])

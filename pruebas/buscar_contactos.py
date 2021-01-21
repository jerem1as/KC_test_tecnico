# https://pypi.org/project/hubspot-api-client/
import requests
import urllib
import json

url = "https://api.hubapi.com/crm/v3/objects/contacts"

querystring = {"limit":"10","paginateAssociations":"false","archived":"false","hapikey":"5adf730a-d272-470f-b6dc-29d96b510e0d","hs_lead_status":"true"}

headers = {'accept': 'application/json'}

req = requests.request("GET", url, headers=headers, params=querystring)

loadedjson = json.loads(req.text)

res = loadedjson["results"]


for testdata in res:

    print (testdata)


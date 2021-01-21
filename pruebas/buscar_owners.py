import requests
import json

apikey= '5adf730a-d272-470f-b6dc-29d96b510e0d'

url = "https://api.hubapi.com/owners/v2/owners?hapikey=" + apikey

r= requests.get(url = url)
response_dict = json.loads(r.text)


for ow in response_dict:


    print ("OWNER: " + str(ow["ownerId"]))
    print ("name: " + str(ow["firstName"]))
    print ("last name: " + str(ow["lastName"]))


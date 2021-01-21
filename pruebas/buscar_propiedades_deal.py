import requests
import json

apikey= '5adf730a-d272-470f-b6dc-29d96b510e0d'

url = "https://api.hubapi.com/deals/v1/deal/3981001643?hapikey=" + apikey

r= requests.get(url = url);
response_dict = json.loads(r.text)

print ("DEAL ID= " + "3981001643")
print ("STATUS: " + str(response_dict["properties"]["dealstage"]["value"]))
print ("Deal Name: " + str(response_dict["properties"]["dealname"]["value"]))
print ("Valor: " + str(response_dict["properties"]["hs_forecast_amount"]["value"]))
print ("Owner ID: " + str(response_dict["properties"]["hubspot_owner_id"]["value"]))
print ("is deleted? " + str(response_dict["isDeleted"]))

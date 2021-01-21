from hubspot3.companies import CompaniesClient
import requests
import json
import urllib




API_KEY = "5adf730a-d272-470f-b6dc-29d96b510e0d"


client = CompaniesClient(api_key=API_KEY)


for company in client.get_all():



    for propiedad in company:

        print (propiedad +": "+ str(company[propiedad]))

    print ("-----------------------------------------------------")

print ("____________________________________________________________________")


import requests
import json
from . import owner
from . import deal

class hubspot_interface:

    def __init__ (self, apikey_):

        self.apikey= apikey_


    def get_owners (self):

        url = "https://api.hubapi.com/owners/v2/owners?hapikey=" + self.apikey
        r= requests.get(url = url)
        print ("Pidiendo owners a HubSpot...")

        response_dict = json.loads(r.text)
        ret = dict()

        for ow in response_dict:

            id_ = ow["ownerId"]
            name_ = ow["firstName"]
            lastname_ = ow["lastName"]

            print ("OWNER: " + str(id_))
            print ("name: " + name_)
            print ("last name: " + lastname_)
            
            tmp = owner.owner(id_,name_, lastname_) 
            ret[id_] = tmp


        return ret
        

    #Los ID y los status se buscan en puntos diferentes de la api. 
    def get_deals_id (self):

        get_all_deals_url = "https://api.hubapi.com/deals/v1/deal/paged?hapikey=" + self.apikey
        ret = []

        r = requests.get(url= get_all_deals_url)
        print ("Pidiendo deal_id a hubspot...")
        response_dict = json.loads(r.text)

        for deal in response_dict["deals"]:
            print ("Encontrado deal_id "+ str(deal["dealId"]))
            ret.append(deal["dealId"])

        return ret

    def get_deal_details(self, deal_id):

        url = "https://api.hubapi.com/deals/v1/deal/" + str(deal_id) + "?hapikey=" + self.apikey

        print ("Buscando detalles para el deal_id " + str(deal_id))
        r= requests.get(url = url);
        response_dict = json.loads(r.text)

        status= str(response_dict["properties"]["dealstage"]["value"])
        name = str(response_dict["properties"]["dealname"]["value"])
        value = str(response_dict["properties"]["hs_forecast_amount"]["value"])
        owner_id = str(response_dict["properties"]["hubspot_owner_id"]["value"])
        is_deleted = str(response_dict["isDeleted"])

        print ("STATUS: " + status)
        print ("Deal Name: " + name)
        print ("Valor: " + value)
        print ("Owner ID: " + owner_id)
        print ("Is deleted? "+ is_deleted)

        #creo el objeto deal
        resp = deal.deal (deal_id, status, name, value, owner_id, is_deleted)

        return resp

    def get_all_deals (self):

        resp = []
        #busco los id de todos los deals
        deal_id_list = self.get_deals_id()
        for deal_id in deal_id_list:
            #traigo los detalles del deal
            deal_tmp = self.get_deal_details(deal_id)
            resp.append(deal_tmp)

        return resp

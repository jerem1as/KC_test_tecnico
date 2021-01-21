from modules import hubspot_interface
from modules import owner
from modules import db


apikey = "5adf730a-d272-470f-b6dc-29d96b510e0d"
db_host = "localhost"
db_user = "cam"
db_pass = "noandanada"
db_schema = "hubspot"

#Busco los owners en hubspot
HI = hubspot_interface.hubspot_interface(apikey)
owners_hubspot = HI.get_owners()

#Inserto los owners en la base
DB = db.DB_interface (db_user, db_schema, db_host, db_pass)
DB.insert_owners (owners_hubspot)

#Busco deals en hubspot
deals = HI.get_all_deals()

#Inserto / Actualizo los deals en la base
DB.insert_deals (deals)



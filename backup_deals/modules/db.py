import mysql.connector


class DB_interface:

    def __init__ (self,user,database,host,passwd):

        self.cnx = mysql.connector.connect (user=user, database=database,host=host,passwd=passwd,auth_plugin='mysql_native_password')



    def insert_owners (self, owners):

       for ow in owners:

            tmp = owners[ow]

            query = "INSERT INTO owners (owner_id,firstname,lastname)"  \
                            "values (" + str(tmp.owner_id) + ",'" + tmp.firstname + \
                            "','" + tmp.lastname + "') " \
                            "on duplicate key update firstname = '" + tmp.firstname + \
                            "',lastname = '" + tmp.lastname + "';"

            cursor = self.cnx.cursor(buffered=True)
            cursor.execute (query)
            self.cnx.commit()
            cursor.close()

    def insert_deals (self, deal_list):

        for deal in deal_list:

            print ("Insertando / Actualizando deal_id: " + str(deal.deal_id))

            query = "INSERT INTO deals (deal_id, status, deal_name, value, owner_id, isdeleted)"\
                    + "values (" + str(deal.deal_id) + ",'" + deal.status + "','" + \
                    deal.name +"'," + deal.value + ",'" + deal.owner_id +"','" \
                    + deal.is_deleted +"')"\
                    + "ON DUPLICATE KEY UPDATE status = '" + deal.status + "'," + \
                    " deal_name = '" + deal.name + "', value = " + deal.value + \
                    " ,owner_id = " + deal.owner_id + ", isdeleted= '" + deal.is_deleted +"';"


            cursor = self.cnx.cursor(buffered=True)
            cursor.execute (query)
            self.cnx.commit()
            cursor.close()



"""
- Insert Statements here
"""
from os import path
from pymongo import MongoClient
import db_utils


class DBConnect:
    """_summary_
    Returns:
        _type_: _description_
    """
    db_uri = str(db_utils.ConstantValue)
    ca_cert = path.join(path.dirname(db_utils.__file__), db_utils.CA_CERTIFICATE_FILE)

    def __init__(self):
        """
        Initializer method for database connection
        """
        self.client = self.__connect()

    def __connect(self):
        return MongoClient(self.__db_uri(), ssl=True)

    def __db_uri(self):
        ca_cert = f'/?tlsCAFile={DBConnect.ca_cert}&maxIdleTimeMS=50000'
        return DBConnect.db_uri + ca_cert

def lambda_handler(event, context):
    """_summary_

    Args:
        event (_type_): _description_
        context (_type_): _description_
    """
    str(event)
    str(context)
    try:
        client = DBConnect().client
        db_name = client['alexandria_General']
        country_master = db_name["Country_Master"]
        response = country_master.find({},{'_id':0})
        ret = []
        for doc in response:
            ret.append(doc)
        client.close()
        return{
            'isError' : True,
            'body' : ret
        }
    except Exception as exception:
        return {
            'isError': True,
            'body': f'Error occurred: {(str(exception))} '
            }
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
import sys

def test_exception():
    try:
        logging.info("dividing 1 by 0")
        x=1/0
    except Exception as e:
        raise SensorException(e,sys)

if __name__ == '__main__':
    try:
        test_exception()
    except Exception as e:
        print(e)
    
    #mongodb_client = MongoDBClient()

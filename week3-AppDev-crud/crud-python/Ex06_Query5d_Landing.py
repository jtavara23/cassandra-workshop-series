#!/usr/bin/env python3
from db_connection import Connection
import datetime
import uuid
#Defining our journey
journey_id = uuid.UUID('f72182dc-cdd4-11ea-9a51-94b86d0d21d0')
spacecraft_name = 'Crew Dragon Endeavour,SpaceX'
print("========================================")
print("Start exercise")
# this is a update statement in python
try:
    connection = Connection()
    connection.session.execute(
        "UPDATE spacecraft_journey_catalog SET active=false, end= %s WHERE spacecraft_name= %s AND journey_id= %s",
        [datetime.datetime.now(), spacecraft_name, journey_id ])
except:
    print('Failure')
else:
    print("Journey {} has now landed".format(str(journey_id)))
    print('Success')
finally:
    connection.close()
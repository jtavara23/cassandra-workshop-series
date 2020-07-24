#!/usr/bin/env python3
from db_connection import Connection
import uuid
import datetime

#Defining our journey
journey_id = uuid.UUID('f72182dc-cdd4-11ea-9a51-94b86d0d21d0')
spacecraft_name = 'Crew Dragon Endeavour,SpaceX'

print("========================================")
print("Start exercise")
print("9..8..7..6..5..4..3..2..1 Ignition")

# this is a update statement in python
try:
    connection = Connection()
    connection.session.execute(
        "UPDATE spacecraft_journey_catalog SET active=true, start= %s WHERE spacecraft_name= %s AND journey_id= %s",
        [datetime.datetime.now(), spacecraft_name, journey_id ])
except Exception as e: 
    print(e)
    print('Failure')
else:
    print("Journey {} has now taken off".format(str(journey_id)))
    print('Success')
finally:
    connection.close()

print('========================================')    
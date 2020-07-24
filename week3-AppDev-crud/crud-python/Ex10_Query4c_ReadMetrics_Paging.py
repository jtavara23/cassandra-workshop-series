#!/usr/bin/env python3
from db_connection import Connection
from cassandra.query import SimpleStatement
import uuid
"""
    spacecraft_speed_over_time has 50 rows for f72182dc-cdd4-11ea-9a51-94b86d0d21d0 in Bettina, so we are going to 
    restrict the number of rows we want to fetch using
    > SimpleStatement(query, fetch_size=5)
"""
print('========================================')
print('Start exercise')

spacecraft_name = 'Bettina'
journey_id      = uuid.UUID('f72182dc-cdd4-11ea-9a51-94b86d0d21d0')

try:
    connection = Connection()
    query      = "select * from spacecraft_speed_over_time where spacecraft_name=%s AND journey_id=%s"
    statement  = SimpleStatement(query, fetch_size=5)
    output = connection.session.execute(statement, [spacecraft_name, journey_id])
    
    print('Page1 with ', len(output.current_rows), ' item(s)')
    for offset in range(0, len(output.current_rows)):
       print("idx=", offset, "time=", output.current_rows[offset].reading_time, "value=", output.current_rows[offset].speed)
    
    print('Paging State=', output.paging_state)
    page2 = connection.session.execute(statement, [spacecraft_name, journey_id], paging_state=output.paging_state)
    
    
    print('Page2 with ', len(page2.current_rows), ' item(s)')
    for offset in range(0, len(page2.current_rows)):
       print("idx=", offset, "time=", page2.current_rows[offset].reading_time, "value=", page2.current_rows[offset].speed)
     
except Exception as e: 
    print(e)
    print('Failure')
else:

    print('Success')
    print('Closing connection (up to 10s)')
finally:
    connection.close()
print('========================================')


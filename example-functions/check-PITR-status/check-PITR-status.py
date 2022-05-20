import json
import os

def lambda_handler(event, context):
    destinationTableName = event['destinationTableName']

    cmd = f"/opt/awscli/aws dynamodb describe-table \
    --table-name {destinationTableName}"
    print(cmd)
    
    returned_value = json.loads(os.system(cmd))
    if (returned_value['Table']['TableStatus'] == "CREATING"):
        print(returned_value)
        print("Table is being created")
        return False
    else:
        print("Table is ready")
        return True
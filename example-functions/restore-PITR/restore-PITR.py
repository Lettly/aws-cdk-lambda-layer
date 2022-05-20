import json
import os

def lambda_handler(event, context):
    destinationTableName = event['destinationTableName']
    sourceTableName = event['sourceTableName']
    restoreTimestamp = event['restoreTimestamp']

    
    cmd = f"/opt/awscli/aws dynamodb restore-table-to-point-in-time \
    --source-table-name {sourceTableName} \
    --target-table-name {destinationTableName} \
    --no-use-latest-restorable-time \
    --restore-date-time {restoreTimestamp}"
    print(cmd)

    returned_value = json.loads(os.system(cmd))
    if (returned_value['TableDescription']['TableName'] == event["destinationTableName"]):
        print(returned_value)
        return returned_value['TableDescription']['TableName']
    else:
        print("Error: Table not restored")
        return "Error: Table not restored"
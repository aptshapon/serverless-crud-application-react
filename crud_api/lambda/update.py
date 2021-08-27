import json
import boto3
import botocore.exceptions as e

cluster_arn = "CLUSTER-ARN"
secret_arn = "SECRET-ARN"
table_name = "proof_of_concept.bookstore"
rdsData = boto3.client("rds-data")


def handler(event, context):
    event_id = event["pathParameters"]
    payload = json.loads(event["body"])

    sql = f'UPDATE {table_name} SET bookname="{payload["bookname"]}", author="{payload["author"]}", price="{payload["price"]}", quantity="{payload["quantity"]}" WHERE id="{event_id["id"]}"'
    try:
        query = rdsData.execute_statement(
            resourceArn=cluster_arn,
            secretArn=secret_arn,
            database="proof_of_concept",
            sql=sql)

        resp = query["numberOfRecordsUpdated"]

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "access-control-allow-origin": "*"
            },
            "body": json.dumps(f"Number of records updated: {resp}")
        }
    except e.ClientError as error:
        raise error

import json
import boto3
import botocore.exceptions as e

cluster_arn = "CLUSTER-ARN"
secret_arn = "SECRET-ARN"
rdsData = boto3.client("rds-data")


def handler(event, context):
    print('event: ', json.dumps(event))

    sql = "insert into bookstore(bookname, author, price, quantity) values(:bookname, :author, :price, :quantity)"

    payload = json.loads(event["body"])

    param1 = {"name": "bookname", "value": {
        "stringValue": payload["bookname"]}}
    param2 = {"name": "author", "value": {"stringValue": payload["author"]}}
    param3 = {"name": "price", "value": {"longValue": int(payload["price"])}}
    param4 = {"name": "quantity", "value": {
        "longValue": int(payload["quantity"])}}

    param_set = [param1, param2, param3, param4]

    try:
        response = rdsData.execute_statement(
            resourceArn=cluster_arn,
            secretArn=secret_arn,
            database="proof_of_concept",
            sql=sql,
            parameters=param_set
        )
        resp = response["numberOfRecordsUpdated"]
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "access-control-allow-origin": "*"
            },
            "body": json.dumps(f"Number of book added: {resp}")
        }
    except e.ClientError as error:
        raise error

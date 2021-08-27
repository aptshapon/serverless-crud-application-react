import json
import boto3

cluster_arn = "CLUSTER-ARN"
secret_arn = "SECRET-ARN"
rdsData = boto3.client("rds-data")
sql = "select * from proof_of_concept.bookstore"


def format_list(response):
    items = {}
    items["Item"] = []
    for record in response["records"]:
        item = {}
        item["id"] = record[0]["longValue"]
        item["bookname"] = record[1]["stringValue"]
        item["author"] = record[2]["stringValue"]
        item["price"] = record[3]["longValue"]
        item["quantity"] = record[4]["longValue"]
        print('Item: ', item)
        items["Item"].append(item)
    return items


def handler(event, context):
    result = rdsData.execute_statement(
        resourceArn=cluster_arn,
        secretArn=secret_arn,
        database="proof_of_concept",
        sql=sql)
    print('result: ', result)

    data = format_list(result)
    resp_body = json.dumps(data["Item"])

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "access-control-allow-origin": "*"
        },
        "body": resp_body
    }
    return response

import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "message": "Welcome to the AWS Serverless API!",
            "module": "Module 05 - AWS Lambda & Serverless",
            "status": "success"
        })
    }

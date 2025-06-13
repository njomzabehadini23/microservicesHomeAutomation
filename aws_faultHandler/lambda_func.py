import json
import boto3

def lambda_handler(event, context):
    # Example fallback logic
    print("Main service down. Taking fallback action...")

    # Simulate alerting
    return {
        'statusCode': 200,
        'body': json.dumps('Fallback action triggered via AWS Lambda')
    }

import boto3
from botocore.exceptions import ClientError
import datetime

LOG_GROUP = 'HomeAutomationLogs'
LOG_STREAM = 'SensorErrorStream'
REGION = 'us-east-1'  # Change if needed

logs = boto3.client('logs', region_name=REGION)

def setup_logs():
    try:
        logs.create_log_group(logGroupName=LOG_GROUP)
    except logs.exceptions.ResourceAlreadyExistsException:
        pass

    try:
        logs.create_log_stream(logGroupName=LOG_GROUP, logStreamName=LOG_STREAM)
    except logs.exceptions.ResourceAlreadyExistsException:
        pass

def log_error(message: str):
    try:
        stream = logs.describe_log_streams(logGroupName=LOG_GROUP, logStreamNamePrefix=LOG_STREAM)
        token = stream['logStreams'][0].get('uploadSequenceToken', None)

        log_event = {
            'logGroupName': LOG_GROUP,
            'logStreamName': LOG_STREAM,
            'logEvents': [{
                'timestamp': int(datetime.datetime.utcnow().timestamp() * 1000),
                'message': message
            }]
        }

        if token:
            log_event['sequenceToken'] = token

        logs.put_log_events(**log_event)
    except ClientError as e:
        print(f"Failed to log to CloudWatch: {e}")

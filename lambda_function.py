import os
import json
import boto3
from datetime import datetime
from sintegra_data import extract_data

def lambda_handler(event, context):
    print(event)
    company_data = extract_data(json.loads(event['body'])['html'])

    sns_arn = os.environ['SINTEGRA_SNS_TOPIC_ARN']
    boto3.client('sns').publish(TopicArn = sns_arn, Message = json.dumps(company_data), Subject='Data from Sintegra [{}]'.format(datetime.now()))

    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps(company_data)
    }

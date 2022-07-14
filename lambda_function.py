import os
import json
import boto3
from sintegra_data import extract_data

def lambda_handler(event, context):

    company_data = extract_data(event['html'])

    sns_arn = os.environ['SINTEGRA_SNS_TOPIC_ARN']
    boto3.client('sns').publish(TopicArn = sns_arn, Message = json.dumps(company_data), Subject='Data from Sintegra')

    return {
        'statusCode': 200,
        'body': json.dumps(company_data)
    }

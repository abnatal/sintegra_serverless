import json
import boto3
from sintegra_data import extract_data

def lambda_handler(event, context):

    company_data = extract_data(event['html'])
    
    sns_client = boto3.client('sns')
    sns_arn = 'arn:aws:sns:sa-east-1:**********:SintegraNotificationTopic'
    sns_client.publish(TopicArn = sns_arn, Message = json.dumps(company_data), Subject='Data from Sintegra')

    return {
        'statusCode': 200,
        'body': json.dumps(company_data)
    }

import json
from sintegra_data import extract_data

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(extract_data(context['html']))
    }

if __name__ == '__main__':
    with open('example.html', 'r') as f:
        context = {'html': f.read()}
    print(lambda_handler(None, context))

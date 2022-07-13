import json
import urllib.request
from bs4 import BeautifulSoup as soup

def lambda_handler(event, context):
    url = 'https://abnatal.com/ip.php'
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    page_html = response.read()
    page_soup = soup(page_html, "html.parser")
    return {
        'statusCode': 200,
        'body': page_soup.text
    }

if __name__ == '__main__':
    print(lambda_handler(None, None))

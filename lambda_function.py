import json
import urllib.parse
import urllib.request
import sys
import os

def lambda_handler(event, context):
    # TODO implement
    message = event['Records'][0]['Sns']['Message']
    LINE_NOTIFY_URL="https://notify-api.line.me/api/notify"
    LINE_NOTIFY_TOKEN= os.environ['LINE_NOTIFY_TOKEN']
    method = "POST"
    headers = {"Authorization": "Bearer %s" % LINE_NOTIFY_TOKEN}
    payload = {"message": message}
    try:
        payload = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(
            url=LINE_NOTIFY_URL, data=payload, method=method, headers=headers)
        urllib.request.urlopen(req)
    except Exception as e:
        print ("Exception Error: ", e)
        sys.exit(1)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
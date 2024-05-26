import boto3
from boto3.dynamodb.conditions import Key
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WatchEvents')

def create_watch_event(user_id, video_id):
    event_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    table.put_item(
        Item={
            'event_id': event_id,
            'user_id': user_id,
            'video_id': video_id,
            'timestamp': timestamp
        }
    )
    return event_id

def get_watch_history(user_id):
    response = table.query(
        IndexName='user_id-timestamp-index',
        KeyConditionExpression=Key('user_id').eq(user_id)
    )
    return response['Items']

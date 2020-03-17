import json
import uuid

queue_url = 'https://sqs.us-east-1.amazonaws.com/051954823249/cloud_obj_detect.fifo'


def get_queue_length(client):
    response = client.get_queue_attributes(
        QueueUrl=queue_url,
        AttributeNames=[
            'ApproximateNumberOfMessages'
        ]
    )
    length = int(response['Attributes']['ApproximateNumberOfMessages'])
    return length


def send_msg(sqs_client, filename, bucket):
    message = {
        'fileName': filename,
        'bucketId': bucket
    }

    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=(
            json.dumps(message)
        ),
        MessageGroupId=str(uuid.uuid1()),
        MessageDeduplicationId=filename[:-5]
    )

    print(response)

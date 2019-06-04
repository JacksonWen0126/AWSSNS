import boto3

sns = boto3.client('sns')

phone_number = '+12223334444'

sns.publish(Message='Hello from AWS SNS',PhoneNumber=phone_number)

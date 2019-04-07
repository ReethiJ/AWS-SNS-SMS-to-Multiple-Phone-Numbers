import boto3
client = boto3.client('sns')

def main():
    numbers=["+91111111111","+91222222222","+1999999999","+91333333333"]
    topicARN = 'ARN-OF-THE-SNS'
    for number in numbers:
        print(number)
        response= client.subscribe(TopicArn = topicARN, Protocol='sms', Endpoint = number)
    client.publish( TopicArn=topicARN, Message="Hello World!")
    return

main()

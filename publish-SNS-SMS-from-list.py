import boto3
client = boto3.client('sns')

def main():
    numbers = ["+91111111111","+91222222222","+1999999999","+91333333333"]
    SMSType = '<Transactional or Promotional>'
    response = client.set_sms_attributes(attributes={'DefaultSMSType':SMSType})
    for number in numbers:
        client.publish( PhoneNumber=number, Message="Hello World!")

main()
# AWS-SNS-SMS-to-Multiple-Phone-Numbers

In order to use SNS to send SMS messages to multiple phone numbers you can either subscribe the phone numbers to the SNS topic and publish your message to that topic or it will be required to use the publish() API call for each phone number. There is no single API call which can be used for this.

You can create a subscription by using the AWS Console:
https://docs.aws.amazon.com/sns/latest/dg/sms_publish-to-topic.html#sms_publish-to-topic_console
If using CLI, you can use the subscribe API:
https://docs.aws.amazon.com/cli/latest/reference/sns/subscribe.html

To do this programmatically, the AWS SDK can be used.
In this repo are samples to do this for Python using Boto3 AWS SDK.

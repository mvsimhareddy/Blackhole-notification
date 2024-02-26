This lambda function fetches the route table details for the specified region and identifies the routes that are in blackhole state and publishes the message to SNS topic, which in return notifes the customer who subscribes to this SNS.

Below is the sample email what customer can see.


Subject:Blackhole Route Detected


Message: Account ID: 46********1
Region: us-west-2
VPC ID: vpc-0d78******c6
Blackhole route found in table rtb-0f******7e: {"DestinationCidrBlock": "2.3.4.5/32", "TransitGatewayId": "tgw-00e1******45", "Origin": "CreateRoute", "State": "blackhole"}

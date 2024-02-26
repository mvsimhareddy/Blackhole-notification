import boto3
import json

def lambda_handler(event, context):

    # Initialize the EC2 client for the specific region

    ec2 = boto3.client('ec2', region_name='us-west-2')


    # Initialize the SNS client for the specifc region

    sns = boto3.client('sns', region_name='us-west-2')

    # Initialize STS to get account details

    sts = boto3.client ('sts')


    # Specify your SNS topic ARN here

    sns_topic_arn = 'enter your SNS topic Arn'


    # Get AWS account Id using STS

    account_id = sts.get_caller_identity().get('Account')

    # Get Region Details

    region = 'us-west-2'

    # Fetching route tables in the region

    response = ec2.describe_route_tables()


    for route_table in response['RouteTables']:
        
        vpc_id = route_table['VpcId']

        print(f"checking route table:{route_table['RouteTableId']} in VPC {vpc_id}")
        
        for route in route_table['Routes']:
            if route.get('State') == 'blackhole':
                print(f"Balckhole route found: {route}")

                # Prepare the message to publish

                message = (
                f"Account ID: {account_id}\n"
                f"Region: {region}\n"
                f"VPC ID: {vpc_id}\n"
                f"Blackhole route found in table {route_table['RouteTableId']}: {json.dumps(route)}"
                )

                # publish the message to the SNS topic

                sns_response = sns.publish(
                    TopicArn=sns_topic_arn,
                    Message=message,
                    Subject='Blackhole Route Detected'
                    )


                print(f"Published message to SNS topic {sns_topic_arn}: {sns_response}")
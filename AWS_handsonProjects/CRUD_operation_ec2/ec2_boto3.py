import  boto3

# Open mangement console
aws_management_console_ec2 = boto3.session.Session(profile_name='default')

# Open ec2 console

ec2_console = aws_management_console_ec2.client(service_name='ec2', region_name='ap-south-1')

# List all the ec2 instances running in the region
# describe_instances method returns the ec2 instances in that region activated by the user

result = ec2_console.describe_instances()['Reservations']

for each_instance in result:
    for value in each_instance['Instances']:
        print(value['InstanceId'])


import boto3


#use of session
'''
Sessions : stores the information about the configuration, credentials, default users etc
           allows  to create services, clients, resources etc.
           


'''
aws_management_console = boto3.session.Session(profile_name = 'default')
iam_console = aws_management_console.resource('iam', region_name = 'ap-south-1')

for user in  iam_console.users.all():
    print(user.name)
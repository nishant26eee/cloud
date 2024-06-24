import boto3

# Replace with your own AWS credentials and region
ACCESS_KEY = 'your_access_key_here'
SECRET_KEY = 'your_secret_key_here'
REGION_NAME = 'your_region_here'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION_NAME)

# List all buckets
response = s3.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

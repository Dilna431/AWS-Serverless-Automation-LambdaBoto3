import boto3
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Initialize a boto3 S3 client
    s3_client = boto3.client('s3')
    
    try:
        # List all S3 buckets
        response = s3_client.list_buckets()
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]
        
        # Loop through each bucket and check if server-side encryption is enabled
        unencryption_buckets = []
        
        for bucket in bucket_names:
            try:
                # Check the encryption status of each bucket
                encryption_response = s3_client.get_bucket_encryption(Bucket=bucket)
                # If encryption is enabled, continue
                if 'ServerSideEncryptionConfiguration' not in encryption_response:
                    unencryption_buckets.append(bucket)
            except s3_client.exceptions.ClientError as e:
                # If encryption information is not available (e.g., no encryption configured), add to the list
                if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFound':
                    unencryption_buckets.append(bucket)
        
        # If there are unencryption buckets, log them
        if unencryption_buckets:
            logger.info("Buckets without encryption: %s", unencryption_buckets)
        else:
            logger.info("All buckets have encryption enabled.")
    
    except Exception as e:
        logger.error("Error occurred: %s", str(e))
        raise e

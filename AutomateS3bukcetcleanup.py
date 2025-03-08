import boto3
import logging
from datetime import datetime, timedelta, timezone

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Initialize boto3 S3 client
    s3 = boto3.client('s3')
    
    # Specify the bucket name
    bucket_name = 'dilna-devops9'  # Replace with your S3 bucket name

    # Calculate the cutoff time (30 days ago) and make it timezone-aware
    cutoff_time = datetime.now(timezone.utc) - timedelta(days=30)
    
    # List objects in the specified S3 bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Check if the response contains 'Contents' (objects in the bucket)
    if 'Contents' in response:
        for obj in response['Contents']:
            # Get the last modified time of the object
            last_modified = obj['LastModified']

            # Check if the object is older than 30 days
            if last_modified < cutoff_time:
                object_key = obj['Key']
                try:
                    # Delete the object from the bucket
                    s3.delete_object(Bucket=bucket_name, Key=object_key)
                    logger.info(f"Deleted object: {object_key}")
                except Exception as e:
                    logger.error(f"Error deleting object {object_key}: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'S3 cleanup function executed successfully'
    }

import boto3
import logging
from datetime import datetime, timedelta

# Initialize S3 client
s3 = boto3.client('s3')
bucket_name = 'dilna-devops9'  # Replace with your S3 bucket name

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Get the current time
    current_time = datetime.now()

    try:
        # List all objects in the S3 bucket
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                # Get the last modified date of the object
                last_modified = obj['LastModified']
                file_name = obj['Key']

                # Calculate the file age (in days)
                file_age = current_time - last_modified.replace(tzinfo=None)
                days_old = file_age.days

                # If the file is older than 6 months (180 days), move to Glacier
                if days_old > 180:
                    logger.info(f"File {file_name} is older than 6 months, changing to Glacier.")

                    # Change the storage class to Glacier
                    s3.copy_object(
                        Bucket=bucket_name,
                        CopySource={'Bucket': bucket_name, 'Key': file_name},
                        Key=file_name,
                        StorageClass='GLACIER'
                    )

                    # Optionally delete the original file to avoid duplicate copies (if needed)
                    # s3.delete_object(Bucket=bucket_name, Key=file_name)
                    logger.info(f"File {file_name} successfully moved to Glacier storage class.")

        else:
            logger.info("No objects found in the bucket.")

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")


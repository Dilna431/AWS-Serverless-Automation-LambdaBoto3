# AWS-Serverless-Automation-LambdaBoto3
This repository contains the solutions for AWS Lambda automation tasks using Boto3. The tasks cover automating EC2 instance management, S3 bucket cleanup, and monitoring unencrypted S3 buckets.

Table of Contents
1.  Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
2.  Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
3.  Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
4.  Assignment 4: 
   
Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
Objective:
Automate the stopping and starting of EC2 instances based on tags using AWS Lambda and Boto3.
Steps:
1. EC2 Setup:
Navigate to the EC2 Dashboard and create two EC2 instances.
Tag the first instance with Key=Action, Value=Auto-Stop.
Tag the second instance with Key=Action, Value=Auto-Start.
2. Lambda IAM Role Setup:
Create a new IAM role for Lambda with the AmazonEC2FullAccess policy.
Attach this IAM role to the Lambda function you will create in the next steps.
3. Lambda Function Creation:
Create a new Lambda function with Python 3.x as the runtime.
Attach the IAM role created above.
Write the Python script to stop instances tagged with Auto-Stop and start instances tagged with Auto-Start. Python file is provided in the repository.
4. Testing:
Manually invoke the Lambda function.
Check the EC2 Dashboard to confirm that the instance tagged Auto-Stop has stopped, and the one tagged Auto-Start has started.

Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
Objective:
Automate the deletion of files older than 30 days in an S3 bucket using AWS Lambda and Boto3.
Steps:
1. S3 Setup:
Create a new S3 bucket.
Upload multiple files to this bucket, ensuring that some files are older than 30 days.
2. Lambda IAM Role Setup:
Create a new IAM role for Lambda with the AmazonS3FullAccess policy.
Attach this IAM role to the Lambda function.
3. Lambda Function Creation:
Create a new Lambda function with Python 3.x as the runtime.
Attach the IAM role created above.
Write the following Boto3 Python script to delete files older than 30 days.
5. Testing:
Manually invoke the Lambda function.
Go to the S3 Dashboard and confirm that only files newer than 30 days remain.

screenshots: 
![image](https://github.com/user-attachments/assets/7c60155d-8584-43c3-a1e9-7d18d748130a)

Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
Objective:
Automate the detection of S3 buckets that don't have server-side encryption enabled using AWS Lambda and Boto3.

Steps:
1. S3 Setup:
Create a few S3 buckets.
Ensure that some buckets don't have server-side encryption enabled.
2. Lambda IAM Role Setup:
Create a new IAM role for Lambda with the AmazonS3ReadOnlyAccess policy.
Attach this IAM role to the Lambda function.
3. Lambda Function Creation:
Create a new Lambda function with Python 3.x as the runtime.
Attach the IAM role created above.
Write the Boto3 Python script to detect unencrypted S3 buckets. Python file is added in the repository.
4. Testing:
Manually invoke the Lambda function.
Review the Lambda logs to identify the buckets without server-side encryption.


Conclusion
These assignments give hands-on experience with AWS Lambda and Boto3 to automate various AWS services, including EC2 instance management, S3 bucket cleanup, and monitoring unencrypted S3 buckets. By automating these tasks, you can improve efficiency and ensure better security and resource management in your AWS environment.

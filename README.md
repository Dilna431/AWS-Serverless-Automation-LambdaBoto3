# AWS-Serverless-Automation-LambdaBoto3
This repository contains the solutions for AWS Lambda automation tasks using Boto3. The tasks cover automating EC2 instance management, S3 bucket cleanup, monitoring unencrypted S3 buckets and Archive Old Files from S3 to Glacier.

Table of Contents
1.  Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
2.  Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
3.  Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
4.  Assignment 4: Archive Old Files from S3 to Glacier Using AWS Lambda and Boto3  
   
# Assignment 1 : Automated Instance Management Using AWS Lambda and Boto3

## Objective

In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. The task is to create a Lambda function that will automatically manage EC2 instances based on their tags. Specifically, you will automate the stopping and starting of EC2 instances using AWS Lambda and Boto3, by detecting their tags.

## Task

You will automate the stopping of EC2 instances with the tag `Auto-Stop` and starting of EC2 instances with the tag `Auto-Start` using AWS Lambda and Boto3.

### Tasks Breakdown:
1. **EC2 Setup**: 
   - Create two EC2 instances with different tags.
   
2. **Lambda Function Creation**:
   - Create an AWS Lambda function with necessary permissions.

3. **Coding**:
   - Implement the logic in Python to stop and start instances based on their tags.

4. **Testing**:
   - Manually trigger the Lambda function and verify if the instances' states are changed according to their tags.

---

## Instructions

### 1. EC2 Setup

1. **Create EC2 Instances**:
   - Navigate to the **EC2** dashboard in the AWS Management Console.
   - Create two **t2.micro instances** or any other available free-tier instance type.
   - You can use the **Amazon Linux 2 AMI** or any other basic AMI.
   - In the instance creation process, select an existing key pair or create a new one for SSH access.

2. **Tag the Instances**:
   - Once the instances are created, navigate to the **Instances** section in the EC2 dashboard.
   - Select the first instance, and click on **Tags**. Add the tag:
     - **Key**: `Action`
     - **Value**: `Auto-Stop`
   - Select the second instance and add the tag:
     - **Key**: `Action`
     - **Value**: `Auto-Start`

---

### 2. Lambda IAM Role

1. **Create a Lambda IAM Role**:
   - Navigate to the **IAM** dashboard in the AWS Management Console.
   - Click on **Roles** from the left-hand menu and then click **Create role**.
   - Choose **Lambda** as the trusted entity type.
   - Attach the **AmazonEC2FullAccess** policy to this role. This policy allows Lambda to start and stop EC2 instances.
   - Click **Next: Tags**, then **Next: Review**, and then **Create role**.
   - Name the role `LambdaEC2Role` (or any descriptive name you prefer).

2. **Assign IAM Role to Lambda Function**:
   - In the next steps, you'll attach this role to the Lambda function when creating it.

---

### 3. Lambda Function

1. **Create a Lambda Function**:
   - Navigate to the **Lambda** dashboard in the AWS Management Console.
   - Click on **Create function**.
   - Choose **Author from scratch**.
   - Provide a name for your Lambda function (e.g., `ManageEC2Instances`).
   - Select **Python 3.x** as the runtime.
   - Under **Permissions**, select **Use an existing role** and choose the IAM role created earlier (`LambdaEC2Role`).
   - Click **Create function**.

2. **Write the Lambda Function Code**:

3. **screenshot**:

![image](https://github.com/user-attachments/assets/5bc57d86-5c8d-4345-af66-e5b2912e0308)

# Assignment 2 : Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

## Objective

In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that automatically deletes files older than 30 days in an S3 bucket.

## Task

Automate the deletion of files older than 30 days in a specific S3 bucket using AWS Lambda and Boto3. This process helps you manage old files and keep your S3 bucket clean and organized.

---

## Instructions

### 1. S3 Setup

1. **Create an S3 Bucket**:
   - Navigate to the **S3** dashboard in the AWS Management Console.
   - Click on **Create bucket**.
   - Provide a globally unique name for the bucket (e.g., `my-s3-bucket-cleanup`).
   - Select a region for the bucket (e.g., `US East (N. Virginia)`).
   - Keep the default settings and click **Create bucket**.

2. **Upload Files to the Bucket**:
   - After the bucket is created, navigate to your bucket in the S3 dashboard.
   - Upload a mix of files to this bucket. Ensure that some files are older than 30 days. You can either:
     - Adjust the system date to simulate older files.
     - Manually upload files that have known ages.
   
---

### 2. Lambda IAM Role

1. **Create an IAM Role for Lambda**:
   - Navigate to the **IAM** dashboard in the AWS Management Console.
   - Click on **Roles** from the left-hand menu and then click **Create role**.
   - Select **Lambda** as the trusted entity type.
   - Attach the **AmazonS3FullAccess** policy to this role. This policy allows Lambda to list, delete, and manage objects in your S3 bucket.
   - Click **Next: Tags**, then **Next: Review**, and then **Create role**.
   - Name the role `LambdaS3CleanupRole` (or any descriptive name you prefer).

2. **Assign IAM Role to Lambda Function**:
   - In the next steps, you'll assign this role to the Lambda function when you create it.

---

### 3. Lambda Function

1. **Create a Lambda Function**:
   - Navigate to the **Lambda** dashboard in the AWS Management Console.
   - Click on **Create function**.
   - Choose **Author from scratch**.
   - Provide a name for your Lambda function (e.g., `S3CleanupFunction`).
   - Select **Python 3.x** as the runtime.
   - Under **Permissions**, select **Use an existing role** and choose the IAM role created earlier (`LambdaS3CleanupRole`).
   - Click **Create function**.

2. **Write the Lambda Function Code**:

3. **screenshot**: 

![image](https://github.com/user-attachments/assets/d96f1dd5-1709-4bc2-adc4-d35a54253c58)

# Assignment 3 : Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3

## Objective

In this assignment, you will enhance your AWS security posture by setting up an AWS Lambda function that detects any S3 bucket without server-side encryption (SSE) enabled. This will help you ensure that all of your S3 buckets are encrypted for better data security.

## Task

Automate the detection of S3 buckets that don't have server-side encryption (SSE) enabled. The Lambda function will list all your S3 buckets, check each one for encryption settings, and log the names of unencrypted buckets.

---

## Instructions

### 1. S3 Setup

1. **Create S3 Buckets**:
   - Navigate to the **S3** dashboard in the AWS Management Console.
   - Click **Create bucket**.
   - Choose a unique name for each bucket (e.g., `unencrypted-bucket-1`, `encrypted-bucket-2`).
   - For a couple of buckets, ensure that **Server-Side Encryption** is not enabled during creation.
   - For a couple of others, enable **Server-Side Encryption (SSE-S3)** to test the detection.

2. **Verify Bucket Encryption Settings**:
   - After creating the buckets, verify the encryption status of each bucket by clicking on the bucket name and going to the **Properties** tab.
   - Under **Server-side encryption**, check whether **SSE-S3** or any other encryption method is enabled o

screenshot:  

![image](https://github.com/user-attachments/assets/c2c96467-89c2-4fde-87c0-10a8e620ab25)  

# Assignment 4: Archive Old Files from S3 to Glacier Using AWS Lambda and Boto3

## Objective

Automate the archival of files older than 6 months from an S3 bucket to Amazon Glacier for cost-effective storage.

## Task

This assignment involves creating an AWS Lambda function that automatically moves files older than 6 months from an S3 bucket to the Glacier storage class.

## Instructions

### 1. S3 Setup

1. **Create an S3 bucket**:
   - Navigate to the **S3** dashboard in the AWS Management Console.
   - Click **Create bucket**.
   - Choose a globally unique bucket name.
   - Configure any additional settings as per your needs.
   - Click **Create bucket**.

2. **Upload files to the bucket**:
   - Upload a mix of old and new files into the newly created S3 bucket. You can use various file types like text, images, or logs.
   - Make sure to upload some files that are older than 6 months for testing.

### 2. Lambda IAM Role

1. **Create a new IAM role for Lambda**:
   - Navigate to the **IAM** dashboard in the AWS Management Console.
   - Click on **Roles** from the left-hand side, then click **Create role**.
   - Select **Lambda** as the trusted entity type.
   - Attach the **AmazonS3FullAccess** policy to this role to grant the Lambda function the necessary permissions to interact with your S3 bucket.
   - Click **Create role** and assign it a name like `LambdaS3FullAccessRole`.

2. **Assign IAM role to Lambda function**:
   - When creating the Lambda function (described in the next step), assign this IAM role to it.

### 3. Lambda Function

1. **Create the Lambda function**:
   - Navigate to the **Lambda** dashboard in the AWS Management Console.
   - Click on **Create function**.
   - Select **Author from scratch**.
   - Name your function (e.g., `ArchiveFilesToGlacier`).
   - Choose Python 3.x as the runtime.
   - Under **Execution role**, select **Use an existing role** and choose the IAM role created in Step 2.

2. **Write the Boto3 Python script**: Python code file is uploaded in the repository

### 4. Screenshot  

![image](https://github.com/user-attachments/assets/df65cde1-e2fb-483a-8425-909173c5ed9f)  

Conclusion
These assignments give hands-on experience with AWS Lambda and Boto3 to automate various AWS services. By automating these tasks, you can improve efficiency and ensure better security and resource management in your AWS environment.

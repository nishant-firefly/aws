# AWS CDK Python App: Step Functions with Lambda and DynamoDB

## Overview

This project demonstrates an AWS CDK application in Python that deploys:
1. A **Lambda** function to call external APIs dynamically using templates stored in DynamoDB.
2. A **DynamoDB** table that stores API templates.
3. A **Step Function** that orchestrates fetching the API template from DynamoDB, calling the Lambda function, and handling the API response.

### Prerequisites

- AWS CLI configured with appropriate credentials.
- AWS CDK installed globally.
- Python 3.x and pip installed.

### Setup

1. **Configure AWS CLI**:

   Ensure that AWS CLI is configured with the appropriate credentials using one of the following methods:

   - **Default AWS CLI profile**:
     ```bash
     aws configure
     ```
     This command will prompt you for:
     - AWS Access Key ID
     - AWS Secret Access Key
     - Default region
     - Default output format

   - **Using AWS Named Profiles**:
     You can configure multiple profiles in your AWS credentials file (`~/.aws/credentials`) and specify which profile to use with CDK by setting the `AWS_PROFILE` environment variable:
     ```bash
     export AWS_PROFILE=my-profile
     ```

   - **Using Environment Variables**:
     Alternatively, you can set AWS credentials using environment variables:
     ```bash
     export AWS_ACCESS_KEY_ID=your-access-key-id
     export AWS_SECRET_ACCESS_KEY=your-secret-access-key
     export AWS_DEFAULT_REGION=your-region
     ```

2. **Install dependencies**:

   Navigate to the project directory and install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Bootstrap your AWS environment** (first time only):

   Before deploying any CDK application, you need to **bootstrap** the environment. This sets up the resources CDK needs to deploy your application:

   ```bash
   cdk bootstrap
   ```

4. **Synthesize the CloudFormation template**:

   Generate the CloudFormation template:

   ```bash
   cdk synth
   ```

5. **Deploy the stack**:

   Deploy the resources to your AWS account:

   ```bash
   cdk deploy
   ```

This will deploy the following resources:
- A DynamoDB table for storing API templates.
- A Lambda function for making API calls.
- A Step Function that orchestrates the entire process.

### AWS CDK Workflow

#### How CDK Works with AWS Configuration

AWS CDK uses **AWS CLI credentials** and configuration to interact with your AWS account, deploying resources like Lambda functions, DynamoDB tables, and Step Functions. CDK synthesizes the AWS infrastructure as **CloudFormation templates** and uses the AWS CLI or SDK to deploy them.

1. **AWS Credentials**:
   - CDK relies on **AWS CLI credentials**. Configure AWS credentials via `aws configure` or environment variables like `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION`.

2. **CDK Workflow**:
   - **Synthesize**: CDK generates a CloudFormation template.
   - **Deploy**: CDK deploys the resources in the AWS account using the AWS CLI credentials.
   - **Execution**: Once deployed, the resources (Lambda, Step Function) are ready to use.

### Cleanup

To delete the stack and all associated resources:

```bash
cdk destroy
```

This will remove all resources deployed by this stack.

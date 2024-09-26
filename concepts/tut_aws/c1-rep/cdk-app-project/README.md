# AWS CDK App: Step Functions with Lambda and DynamoDB

## Overview

This project demonstrates an AWS CDK application that deploys:
1. A **Lambda** function to call external APIs dynamically using templates stored in DynamoDB.
2. A **DynamoDB** table that stores API templates.
3. A **Step Function** that orchestrates fetching the API template from DynamoDB, calling the Lambda function, and handling the API response.

### Prerequisites

- AWS CLI configured with appropriate credentials.
- AWS CDK installed globally.
- Node.js and npm installed.
  
### Setup

1. Clone this repository and navigate to the project directory.
2. Install dependencies:

   ```bash
   npm install
   ```

3. Build the project:

   ```bash
   npm run build
   ```

### Deploy

To deploy the stack:

```bash
cdk deploy
```

This will deploy the following resources:
- A DynamoDB table for storing API templates.
- A Lambda function for making API calls.
- A Step Function that orchestrates the entire process.

### Cleanup

To delete the stack:

```bash
cdk destroy
```

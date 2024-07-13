# Set Up System

Welcome to the setup guide for our system. This document provides instructions for setting up your local environment using LocalStack and Docker. Please follow the steps outlined below to configure and start your services.

## Installation

### LocalStack with Docker

For a detailed installation guide for LocalStack, please refer to our [Installation Document](https://docs.google.com/document/d/1o_DJDGDltexrNTf4f1FwmJNnVJGHw6XuyiyKcsxeGN4/edit?usp=sharing).

## Configuration

### One-Time Setup: Generating Environment Variables

Before you begin using the system, you need to generate a `.env` file that will store your AWS credentials and other configuration settings from `config.json`. This is a one-time setup process, necessary for initializing your environment.

#### Install Dependencies 
```bash
# Assuming python3.11+ is installed 
cd path/to/up_system
## Can create virual environment and run 
python -m pip install -r requirements.txt
```
#### Generate AWS Credentials and Configuration

To create the `.env` file with AWS secrets, keys, and configurations, run the following command. This will setup the initial configuration and generate new AWS credentials:

```bash
# Navigate to the system setup directory
cd path/to/up_system

# Generate environment variables and AWS credentials
python generate_env.py --change-aws-creds
```

## Running the System
Once the configuration is in place, you can start LocalStack to simulate the AWS environment on your local machine:

### Start LocalStack services with Docker Compose 
```bash
# Navigate to the LocalStack directory
cd path/to/up_system
docker-compose up
```

### Routine Configuration Updates
If you need to update the values from config.json into the .env file after the initial setup, you can do so by running the following command:

```bash
# Navigate to the system setup directory
cd path/to/up_system

# Update configuration in the .env file
python generate_env.py
```


# Service Status Checker (check_system.py)

This Python script `check_system.py` checks the status of various services, in a sequence:
1. Docker
2. Localstack [TODO]
3. AWS Services [TODO]
    - S3
    - IAM
```bash
python check_system.py
``` 

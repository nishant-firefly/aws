import boto3
import os
from utils import RunningStatus, Service
from service_aws import AwsService

class S3(AwsService):
    def __init__(self):
        # self.boto_client will be initiated 
        super().__init__("s3")

if __name__=="__main__":
    s3=S3()
    print(s3.client)
    breakpoint()



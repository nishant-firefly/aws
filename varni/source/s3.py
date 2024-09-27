import boto3

class S3Handler(BaseSource):
    def __init__(self, bucket_name, user, permissions):
        super().__init__(user, permissions)
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name

    @BaseSource.permission_required("read")
    def read(self, entity_name, columns, key):
        """Download a file from S3"""
        obj = self.s3.get_object(Bucket=self.bucket_name, Key=key)
        return obj['Body'].read()

    @BaseSource.permission_required("write")
    def create(self, entity_name, columns, key, data):
        """Upload a new file to S3"""
        self.s3.put_object(Bucket=self.bucket_name, Key=key, Body=data)

    @BaseSource.permission_required("write")
    def update(self, entity_name, columns, key, data):
        """Update an existing file in S3"""
        self.create(entity_name, columns, key, data)

    @BaseSource.permission_required("write")
    def delete(self, entity_name, columns, key):
        """Delete a file from S3"""
        self.s3.delete_object(Bucket=self.bucket_name, Key=key)

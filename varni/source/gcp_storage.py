from .source import BaseSource
from google.cloud import storage

class GCPHandler(BaseSource):
    def __init__(self, bucket_name, user, permissions):
        super().__init__(user, permissions)
        self.client = storage.Client()  # Assuming GCP credentials are already set up
        self.bucket = self.client.get_bucket(bucket_name)

    @BaseSource.permission_required("read")
    def read(self, entity_name, columns, blob_name):
        """Download a blob from Google Cloud Storage"""
        blob = self.bucket.blob(blob_name)
        content = blob.download_as_string()
        return content

    @BaseSource.permission_required("write")
    def create(self, entity_name, columns, blob_name, data):
        """Upload a new blob to Google Cloud Storage"""
        blob = self.bucket.blob(blob_name)
        blob.upload_from_string(data)

    @BaseSource.permission_required("write")
    def update(self, entity_name, columns, blob_name, data):
        """Update an existing blob in Google Cloud Storage"""
        self.create(entity_name, columns, blob_name, data)

    @BaseSource.permission_required("write")
    def delete(self, entity_name, columns, blob_name):
        """Delete a blob from Google Cloud Storage"""
        blob = self.bucket.blob(blob_name)
        blob.delete()

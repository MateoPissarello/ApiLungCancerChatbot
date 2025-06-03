import boto3
import os
from fastapi import HTTPException
from utils.utils import bytes_to_file


class FileHandler:
    def __init__(self, bucket_name):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION"),
        )
        self.bucket_name = bucket_name

    def upload_file(self, contents, filename, content_type):
        try:
            self.s3.upload_fileobj(
                Fileobj=bytes_to_file(contents),
                Bucket=self.bucket_name,
                Key=filename,
                ExtraArgs={"ContentType": content_type},
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to upload file to S3: {str(e)}",
            )
        return f"https://{self.bucket_name}.s3.amazonaws.com/{filename}"

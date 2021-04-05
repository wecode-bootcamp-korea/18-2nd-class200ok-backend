from storages.backends.s3boto3 import S3Boto3Storage

from my_settings    import AWS_STORAGE_BUCKET_NAME

class MediaStorage(S3Boto3Storage):
    bucket_name = AWS_STORAGE_BUCKET_NAME

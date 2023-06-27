from minio import Minio

client = Minio(
    "minio.davud.ru",
    access_key="YBPgiw5mGt4kyrJB",
    secret_key="LHIywTMipIkXYHLGn987lzfzel5Srtrr",
)

buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name)

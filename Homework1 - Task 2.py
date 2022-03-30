import boto3
def main():
        s3 = boto3.resource('s3')
        filtered_buckets = filter(lambda bucket: bucket.name.startswith("prod"), s3.buckets.all())
        for bucket in filtered_buckets:
                print(bucket.name)
if __name__ == '__main__':
	main()
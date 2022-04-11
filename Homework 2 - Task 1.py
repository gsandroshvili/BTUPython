import boto3

from argparse import ArgumentParser

def parser():
    parser = ArgumentParser()
    parser.add_argument('-n', '--name', type=str, required=True)        
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def exists(s3, name):
    response = s3.head_bucket(Bucket=name)
    return response["ResponseMetadata"]["HTTPStatusCode"] == 200

def create():
    parsed_arguments = parser()
    name = parsed_arguments.name
    s3 = boto3.client('s3')
    if exists(s3, name):
        print(f"Bucket exists")
    else:
        s3.create_bucket(Bucket=name)

if __name__ == '__main__':
    create()
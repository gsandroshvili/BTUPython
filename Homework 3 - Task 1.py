from argparse import ArgumentParser
import boto3
import os

def parser():
    parser = ArgumentParser()
    parser.add_argument("-n", "--name", type=str, required=True)
    parser.add_argument("-b", "--bucket", type=str, required=True)
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def upload():
    parsed_arguments = parser()
    s3 = boto3.client("s3")
    object_name = os.path.basename(parsed_arguments.name)
    s3.upload_file(parsed_arguments.name, parsed_arguments.bucket, object_name)

if __name__ == '__main__':
    upload()
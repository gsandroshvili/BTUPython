from argparse import ArgumentParser
import boto3
import os

def parser():
    parser = ArgumentParser()
    parser.add_argument("-n", "--name", type=str, required=True)
    parser.add_argument("-b", "--bucket", type=str, required=True)
    parser.add_argument("-p", "--path", type=str, required=False, default="./")
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def download():
    parsed_arguments = parser()
    s3 = boto3.client("s3")
    path = os.path.join(parsed_arguments.path, parsed_arguments.name)
    s3.download_file(parsed_arguments.bucket, parsed_arguments.name, path)

if __name__ == '__main__':
    download()
from argparse import ArgumentParser
import boto3

def parser():
    parser = ArgumentParser()
    parser.add_argument("-n", "--name", type=str, required=True)
    parser.add_argument("-b", "--bucket", type=str, required=True)
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def delete():
    parsed_arguments = parser()
    s3 = boto3.client("s3")
    s3.delete_object(Bucket=parsed_arguments.bucket, Key=parsed_arguments.name)

if __name__ == '__main__':
    delete()
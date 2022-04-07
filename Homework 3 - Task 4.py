from argparse import ArgumentParser
import boto3
import os

def parser():
    parser = ArgumentParser()
    parser.add_argument("-b", "--bucket", type=str, required=True)
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def print_types():
    parsed_arguments = parser()
    bucket = parsed_arguments.bucket
    s3 = boto3.client("s3")
    objects = s3.list_objects(Bucket=bucket)
    temp_dict_count = {}

    for object in objects.get('Contents', []):
        name = object.get('Key')
        nameResult = os.path.splitext(name)[1].lower()
        if nameResult in temp_dict_count:
            temp_dict_count[nameResult] += 1
        else:
            temp_dict_count[nameResult] = 1

    for name in temp_dict_count:
        count = temp_dict_count[name]
        print(f'{name}-{count}')

if __name__ == '__main__':
    print_types()
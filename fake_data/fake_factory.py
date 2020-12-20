import random
import csv
import boto3
from faker import Faker
from django.core.files import File
from dummy_data_project.settings import *


def gen_fake_data(data, filename, row_num):
    fake = Faker()
    id = data['id']
    data.pop('id')
    data.pop('title')
    data.pop('modified')
    rows = []
    for _ in range(row_num):
        field = []
        row = []
        for k, v in data.items():
            if data[k]:
                field.append(k)
                fake_method = getattr(fake, k)
                item = fake_method()
                row.append(item)
        rows.append(row)

    with open(filename, 'w') as csvfile:
        myfile = File(csvfile)
        csvwriter = csv.writer(myfile)
        csvwriter.writerow(field)
        csvwriter.writerows(rows)

    s3_client = boto3.client('s3')
    with open(filename, "rb") as f:
        s3_client.upload_fileobj(f, AWS_STORAGE_BUCKET_NAME,
                                 filename, ExtraArgs={'ACL': 'public-read'})

import random
import csv
import boto3
from faker import Faker
from django.core.files import File
from dummy_data_project.settings import *


class FakeDataGen():
    pass


def gen_fake_data(data, filename):
    fake = Faker()
    row_num = int(data['row_num'])
    id = data['id']
    data.pop('row_num')
    data.pop('id')
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

    s3 = boto3.resource('s3')
    data = open(filename, 'rb')
    try:
        s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(Key=filename, Body=data)
    except Exception as e:
        raise IOError(e)


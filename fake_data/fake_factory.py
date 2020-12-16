# from faker import Faker
# import random
# import csv
# from django.core.files import File


# class FakeDataGen():
#     pass


# def gen_fake_data(data, filename):
#     fake = Faker()
#     row_num = int(data['row_num'])
#     id = data['id']
#     data.pop('row_num')
#     data.pop('id')
#     rows = []
#     for _ in range(row_num):
#         field = []
#         row = []
#         for k, v in data.items():
#             if data[k]:
#                 field.append(k)
#                 fake_method = getattr(fake, k)
#                 item = fake_method()
#                 row.append(item)
#         rows.append(row)

#     with open(filename, 'wb') as csvfile:
#         myfile = File(csvfile)
#         csvwriter = csv.writer(myfile)
#         csvwriter.writerow(field)
#         csvwriter.writerows(rows)


from faker import Faker
import random
import csv
import io
import json
import base64
import boto3
from django.core.files import File
from dummy_data_project.storage_settings import AWS_STORAGE_BUCKET_NAME


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

    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(field)
    writer.writerows(rows)

    file_content = base64.standard_b64decode(output.getvalue())
    file_path = filename
    s3 = boto3.client('s3')
    try:
        s3_response = s3.put_object(
            Bucket=AWS_STORAGE_BUCKET_NAME, Key=file_path, Body=file_content)
    except Exception as e:
        raise IOError(e)
    # return {
    #     'statusCode': 200,
    #     'body': {
    #         'file_path': file_path
    #     }
    # }

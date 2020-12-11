from faker import Faker
import random
import csv


class FakeDataGen():
    def __init__(self, integer=99):
        fake = Faker()
        self.full_name = fake.name()
        self.job = fake.job()
        self.email = fake.email()
        self.phone_number = fake.phone_number()
        self.company_name = fake.company()
        self.text = fake.text()
        self.integer = random.randint(0, integer)
        self.date = fake.date_time()
        self.address = fake.address()


def gen_fake_data(numRows):
    filename = 'fake_data.csv'
    rows = []
    for _ in range(numRows):
        data = FakeDataGen()
        field = data.__dict__.keys()
        row = list(data.__dict__.values())
        rows.append(row)
    fields = field

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

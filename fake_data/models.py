from django.db import models


class FakeDataModel(models.Model):
    model = models.ForeignKey('SchemaDataModel', on_delete=models.CASCADE)
    file = models.FileField(null=True, upload_to='files')


class SchemaDataModel(models.Model):
    full_name = models.BooleanField(null=False, default=True)
    email = models.BooleanField(null=False, default=True)
    phone_number = models.BooleanField(null=False, default=True)
    company_name = models.BooleanField(null=False, default=True)
    text = models.BooleanField(null=False, default=True)
    integer = models.BooleanField(null=False, default=True)
    date = models.BooleanField(null=False, default=True)
    address = models.BooleanField(null=False, default=True)

    row_num = models.IntegerField(null=False, default=True)

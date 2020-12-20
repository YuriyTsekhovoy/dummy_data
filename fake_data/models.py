import os
from django.db import models
from django.db.models.signals import post_save
from django.core.files import File
from dummy_data_project.celery import generate
from dummy_data_project.storage_settings import STATIC_URL
from dummy_data_project.settings import *
from time import gmtime, strftime


class FakeDataModel(models.Model):
    model = models.ForeignKey('SchemaDataModel', on_delete=models.CASCADE)
    row_num = models.PositiveIntegerField(null=False, default=True)
    url = models.URLField(null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        filename = gen_filename()
        url = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{filename}"
        self.url = url
        super().save(*args, **kwargs)

    def __str__(self):
        return self.model.title + ', ' + str(self.row_num) + ' items'


def gen_filename():
    filename = os.path.join('static', 'files', 'fake_data_{}.csv'.format(
        strftime("%Y_%m_%d_%H_%M_%S", gmtime())))
    return filename


def fakedata_post_save(sender, instance, signal, *args, **kwargs):
    if instance:
        data_dict = instance.model.__dict__
        data_dict.pop('_state')
        row_num = instance.row_num
        filename = instance.url.split('https://dummy-d.s3.amazonaws.com/')[-1]
        generate(data_dict, filename, row_num)


post_save.connect(fakedata_post_save, sender=FakeDataModel)


class SchemaDataModel(models.Model):
    title = models.CharField(max_length=255)
    modified = models.DateField(auto_now=True)
    name = models.BooleanField(null=False, default=True)
    email = models.BooleanField(null=False, default=True)
    phone_number = models.BooleanField(null=False, default=True)
    company = models.BooleanField(null=False, default=True)
    text = models.BooleanField(null=False, default=True)
    random_int = models.BooleanField(null=False, default=True)
    date = models.BooleanField(null=False, default=True)
    address = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.title

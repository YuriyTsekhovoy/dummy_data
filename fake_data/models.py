import os
from django.db import models
from django.db.models.signals import pre_save
from dummy_data_project.celery import generate
from fake_data.fake_factory import FakeDataGen, gen_fake_data
from dummy_data_project.storage_settings import STATIC_URL
# from dummy_data_project.settings import MEDIA_ROOT
from time import gmtime, strftime


class FakeDataModel(models.Model):
    model = models.ForeignKey('SchemaDataModel', on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True, upload_to='files')
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     fake_file = self.file.url(self.file.path)
    #     fake_file.save(self.file.path)

def fakedata_pre_save(sender, instance, signal, *args, **kwargs):

    if instance:

        data_dict = instance.model.__dict__
        data_dict.pop('_state')

        filename = os.path.join('static', 'files', 'fake_data_{}.csv'.format(
            strftime("%Y_%m_%d_%H_%M_%S", gmtime())))

        gen_fake_data(data_dict, filename)
        print(instance)

        # instance.save()
pre_save.connect(fakedata_pre_save, sender=FakeDataModel)


class SchemaDataModel(models.Model):
    name = models.BooleanField(null=False, default=True)
    email = models.BooleanField(null=False, default=True)
    phone_number = models.BooleanField(null=False, default=True)
    company = models.BooleanField(null=False, default=True)
    text = models.BooleanField(null=False, default=True)
    random_int = models.BooleanField(null=False, default=True)
    date = models.BooleanField(null=False, default=True)
    address = models.BooleanField(null=False, default=True)

    row_num = models.IntegerField(null=False, default=True)

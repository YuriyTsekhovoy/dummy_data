# Generated by Django 3.1.4 on 2020-12-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_data', '0003_auto_20201213_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakedatamodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
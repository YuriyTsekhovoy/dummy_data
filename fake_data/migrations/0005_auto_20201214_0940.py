# Generated by Django 3.1.4 on 2020-12-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_data', '0004_auto_20201213_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakedatamodel',
            name='file',
            field=models.FileField(default='default.cvs', upload_to='files'),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_data', '0003_auto_20201210_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemadatamodel',
            name='address',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='schemadatamodel',
            name='company_name',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='schemadatamodel',
            name='date',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='schemadatamodel',
            name='email',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='schemadatamodel',
            name='full_name',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='schemadatamodel',
            name='integer',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='schemadatamodel',
            name='phone_number',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='schemadatamodel',
            name='row_num',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='schemadatamodel',
            name='text',
            field=models.BooleanField(default=True),
        ),
    ]

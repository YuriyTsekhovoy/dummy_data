# Generated by Django 3.1.4 on 2020-12-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_data', '0007_auto_20201219_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakedatamodel',
            name='url',
            field=models.URLField(blank=True, editable=False, null=True),
        ),
    ]

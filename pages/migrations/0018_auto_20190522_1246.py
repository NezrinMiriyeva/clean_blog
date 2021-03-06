# Generated by Django 2.2.1 on 2019-05-22 12:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20190522_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='sub_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

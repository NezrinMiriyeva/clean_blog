# Generated by Django 2.2.1 on 2019-05-17 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20190517_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitecommon',
            name='offer_background',
        ),
    ]

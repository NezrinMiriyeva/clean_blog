# Generated by Django 2.2.1 on 2019-06-29 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0037_auto_20190629_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='background_image',
            new_name='image',
        ),
    ]
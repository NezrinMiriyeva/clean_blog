# Generated by Django 2.2.1 on 2019-05-21 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20190521_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sub_title',
        ),
    ]

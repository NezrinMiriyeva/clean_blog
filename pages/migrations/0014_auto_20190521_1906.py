# Generated by Django 2.2.1 on 2019-05-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20190521_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='background_image',
            field=models.ImageField(upload_to='post/'),
        ),
    ]

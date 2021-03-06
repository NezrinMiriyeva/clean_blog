# Generated by Django 2.2.1 on 2019-05-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20190520_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('background_image', models.ImageField(upload_to='about/')),
            ],
        ),
    ]

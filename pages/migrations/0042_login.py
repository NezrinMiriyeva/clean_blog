# Generated by Django 2.2.1 on 2019-07-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0041_auto_20190702_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='login/')),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_delete_authorprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]

# Generated by Django 2.2.1 on 2019-07-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0040_auto_20190629_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
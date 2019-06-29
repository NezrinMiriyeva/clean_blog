# Generated by Django 2.2.1 on 2019-06-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_articles_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='image',
        ),
        migrations.AddField(
            model_name='articles',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/'),
        ),
    ]
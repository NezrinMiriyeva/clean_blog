# Generated by Django 2.2.1 on 2019-06-20 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_articles_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='text',
        ),
    ]

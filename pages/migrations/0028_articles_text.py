# Generated by Django 2.2.1 on 2019-06-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_delete_myarticles'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='text',
            field=models.TextField(default=0),
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0038_auto_20190629_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
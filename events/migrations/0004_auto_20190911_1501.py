# Generated by Django 2.2 on 2019-09-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190911_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='api_url',
            field=models.CharField(max_length=255),
        ),
    ]

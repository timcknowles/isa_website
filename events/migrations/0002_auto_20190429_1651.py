# Generated by Django 2.1 on 2019-04-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_code',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='event_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

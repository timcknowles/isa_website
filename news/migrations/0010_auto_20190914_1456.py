# Generated by Django 2.2 on 2019-09-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20190914_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='intro',
            field=models.CharField(blank=True, max_length=250, verbose_name='one line summary'),
        ),
    ]

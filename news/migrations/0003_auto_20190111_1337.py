# Generated by Django 2.0.7 on 2019-01-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190111_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='first_name',
            field=models.CharField(blank=True, max_length=250, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='last_name',
            field=models.CharField(blank=True, max_length=250, verbose_name='Last name'),
        ),
    ]

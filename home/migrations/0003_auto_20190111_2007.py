# Generated by Django 2.0.7 on 2019-01-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190111_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]

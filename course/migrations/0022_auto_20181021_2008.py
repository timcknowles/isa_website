# Generated by Django 2.0.7 on 2018-10-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0021_auto_20181021_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepage',
            name='start_date',
            field=models.DateTimeField(blank=True, help_text='testing'),
        ),
    ]

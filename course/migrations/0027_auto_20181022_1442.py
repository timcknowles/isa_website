# Generated by Django 2.0.7 on 2018-10-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0026_auto_20181022_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepage',
            name='end_date',
            field=models.DateTimeField(blank=True, help_text='for courses with consecutive dates', null=True),
        ),
    ]

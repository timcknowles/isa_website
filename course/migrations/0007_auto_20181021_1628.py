# Generated by Django 2.0.7 on 2018-10-21 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20181021_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursepage',
            old_name='person',
            new_name='contact_details',
        ),
    ]
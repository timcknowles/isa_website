# Generated by Django 2.2 on 2019-09-14 16:03

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20190914_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsindexpage',
            name='thanks_info',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
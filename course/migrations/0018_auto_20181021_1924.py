# Generated by Django 2.0.7 on 2018-10-21 18:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_auto_20181021_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepage',
            name='dates',
            field=wagtail.core.fields.StreamField([('date_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('date', wagtail.core.blocks.DateBlock()), ('description', wagtail.core.blocks.CharBlock())], icon='user')))], blank=True),
        ),
    ]
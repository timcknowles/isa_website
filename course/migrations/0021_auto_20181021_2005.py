# Generated by Django 2.0.7 on 2018-10-21 19:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_auto_20181021_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepage',
            name='dates',
            field=wagtail.core.fields.StreamField([('date_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('date', wagtail.core.blocks.DateBlock()), ('description', wagtail.core.blocks.CharBlock())])))], blank=True),
        ),
    ]
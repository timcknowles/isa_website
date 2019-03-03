# Generated by Django 2.1 on 2019-03-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20190303_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='A slug to identify posts by this category', max_length=255, null=True, verbose_name='slug'),
        ),
    ]

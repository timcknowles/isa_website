# Generated by Django 2.1 on 2019-03-03 17:45

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('news', '0006_auto_20190303_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AddField(
            model_name='newspage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='news.Category'),
        ),
    ]
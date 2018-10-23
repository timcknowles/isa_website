# Generated by Django 2.0.7 on 2018-10-23 08:32

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0028_coursepagerelatedlinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePageRelatedDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('date', models.DateField(blank=True, verbose_name='Course Date')),
                ('description', models.CharField(max_length=255)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_dates', to='course.CoursePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]

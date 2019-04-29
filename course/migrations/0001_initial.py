# Generated by Django 2.0.7 on 2019-04-29 16:37

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.table_block.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Courses & Conferences Index Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CoursePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', models.CharField(max_length=250, verbose_name='one line summary')),
                ('summary', wagtail.core.fields.RichTextField(verbose_name='full summary')),
                ('address_details', models.CharField(blank=True, max_length=250, verbose_name='address details')),
                ('formatted_address', models.CharField(max_length=255)),
                ('course_flyer', wagtail.core.fields.StreamField([('course_flyer', wagtail.documents.blocks.DocumentChooserBlock())], blank=True)),
                ('organiser_name', models.CharField(blank=True, max_length=250, verbose_name='name')),
                ('organiser_email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('organiser_number', models.CharField(blank=True, max_length=250, verbose_name='number')),
                ('course_programme', wagtail.core.fields.StreamField([('table', wagtail.contrib.table_block.blocks.TableBlock())], blank=True)),
                ('course_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Courses & Conferences Page',
            },
            bases=('wagtailcore.page',),
        ),
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
        migrations.CreateModel(
            name='CoursePageRelatedLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=255)),
                ('link_external', models.URLField(blank=True, verbose_name='External link')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_links', to='course.CoursePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]

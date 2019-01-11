# Generated by Django 2.0.7 on 2019-01-11 09:56

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', models.CharField(max_length=250, verbose_name='one line summary')),
                ('summary', wagtail.core.fields.RichTextField(verbose_name='full summary')),
                ('display_until', models.DateField(verbose_name='display until')),
                ('organiser_name', models.CharField(blank=True, max_length=250, verbose_name='name')),
                ('organiser_email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('organiser_number', models.CharField(blank=True, max_length=250, verbose_name='number')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
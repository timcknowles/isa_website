# Generated by Django 2.2 on 2019-11-12 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='event_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]
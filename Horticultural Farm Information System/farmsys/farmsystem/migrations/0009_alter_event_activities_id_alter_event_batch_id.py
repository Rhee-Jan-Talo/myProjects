# Generated by Django 4.0.5 on 2022-08-09 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsystem', '0008_rename_title_event_activity_event_plant_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='activities_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='batch_id',
            field=models.IntegerField(),
        ),
    ]

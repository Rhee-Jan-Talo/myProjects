# Generated by Django 4.1 on 2022-10-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsystem', '0047_alter_event_activity_alter_event_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='activities_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

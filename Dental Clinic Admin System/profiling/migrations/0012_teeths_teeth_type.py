# Generated by Django 3.2.7 on 2021-09-28 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0011_teeths_teeths_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='teeths',
            name='teeth_type',
            field=models.CharField(default='Adult', max_length=200),
        ),
    ]

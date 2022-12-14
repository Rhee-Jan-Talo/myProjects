# Generated by Django 4.1 on 2022-09-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsystem', '0038_rename_redelivery_details_model_redelivery_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='redelivery_info_update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('re_delivery_status', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=200)),
                ('date_arrived', models.CharField(max_length=200)),
                ('date_shipped', models.CharField(max_length=200)),
                ('expected_arrival', models.CharField(max_length=200)),
            ],
        ),
    ]

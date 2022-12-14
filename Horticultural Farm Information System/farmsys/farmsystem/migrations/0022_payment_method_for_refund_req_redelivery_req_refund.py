# Generated by Django 4.0.5 on 2022-08-18 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsystem', '0021_purchase_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_method_for_refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refund_id', models.IntegerField()),
                ('payment_method', models.CharField(max_length=200)),
                ('payment_for', models.CharField(max_length=200)),
                ('account_num', models.CharField(max_length=200)),
                ('account_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='req_redelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transac_id', models.IntegerField()),
                ('quan_received', models.IntegerField()),
                ('returned_quan', models.IntegerField()),
                ('reason_rd', models.CharField(max_length=200)),
                ('proof_pic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='req_refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transac_id', models.IntegerField()),
                ('quantity_received', models.IntegerField()),
                ('refund_quan', models.IntegerField()),
                ('reason_refund', models.CharField(max_length=200)),
                ('proof_refund', models.ImageField(upload_to='')),
            ],
        ),
    ]

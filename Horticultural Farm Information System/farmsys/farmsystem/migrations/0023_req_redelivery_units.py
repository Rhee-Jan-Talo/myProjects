# Generated by Django 4.0.5 on 2022-08-19 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsystem', '0022_payment_method_for_refund_req_redelivery_req_refund'),
    ]

    operations = [
        migrations.AddField(
            model_name='req_redelivery',
            name='units',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
    ]

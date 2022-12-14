# Generated by Django 4.1 on 2022-09-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsystem', '0026_payments_amount_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_order_confirmed',
            name='user_id',
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='balance_to_pay',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='cancel_date',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='cancel_reason',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='confirmed_quantity',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='delivery_fee',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='dp_due',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='dp_paid',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='dp_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='expected_date_arrival',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='fp_paid',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='fullpayment_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='harvest_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='is_cancelled',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='is_user_confirmed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='total_amount',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='total_downpayment',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='u_order_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_order_confirmed',
            name='units',
            field=models.CharField(default='0', max_length=200),
        ),
    ]

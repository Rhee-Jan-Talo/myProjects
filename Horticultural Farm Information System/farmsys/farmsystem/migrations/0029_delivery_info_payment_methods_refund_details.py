# Generated by Django 4.1 on 2022-09-02 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsystem', '0028_user_order_confirmed_plant_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivery_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_order_id', models.IntegerField()),
                ('delivery_status', models.CharField(default='Ongoing', max_length=200)),
                ('details', models.CharField(max_length=1000)),
                ('date_arrived', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='payment_methods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_order_id', models.IntegerField()),
                ('payment_method', models.CharField(max_length=200)),
                ('payment_for', models.CharField(default='0', max_length=200)),
                ('account_number', models.CharField(max_length=200)),
                ('account_name', models.CharField(max_length=200)),
                ('proof_receipt', models.CharField(default='0', max_length=200)),
                ('is_selected', models.CharField(default='0', max_length=200)),
                ('amount_paid', models.CharField(default='0', max_length=200)),
                ('date_paid', models.CharField(default='0', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='refund_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_order_id', models.IntegerField()),
                ('date_from', models.CharField(max_length=200)),
                ('date_to', models.CharField(max_length=200)),
                ('refund_percentage', models.CharField(max_length=200)),
            ],
        ),
    ]

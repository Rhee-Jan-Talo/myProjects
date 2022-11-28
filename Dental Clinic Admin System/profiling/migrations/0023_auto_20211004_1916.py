# Generated by Django 3.2.7 on 2021-10-04 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0022_auto_20210930_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_inventory',
            name='barcode',
            field=models.CharField(default='00000000', max_length=100),
        ),
        migrations.AlterField(
            model_name='item_inventory',
            name='expiry_status',
            field=models.CharField(default='Good for usage', max_length=200),
        ),
    ]

# Generated by Django 3.2.7 on 2021-11-26 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0038_alter_stock_in_total_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_in',
            name='total_payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

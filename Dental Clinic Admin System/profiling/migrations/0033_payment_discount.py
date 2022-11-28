# Generated by Django 3.2.7 on 2021-11-24 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0032_prescription_purchase_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

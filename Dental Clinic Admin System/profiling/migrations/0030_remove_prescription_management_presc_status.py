# Generated by Django 3.2.7 on 2021-10-17 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0029_alter_accounts_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription_management',
            name='presc_status',
        ),
    ]

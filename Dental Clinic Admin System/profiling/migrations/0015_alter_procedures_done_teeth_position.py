# Generated by Django 3.2.7 on 2021-09-28 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0014_remove_teeths_teeth_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedures_done',
            name='teeth_position',
            field=models.ForeignKey(db_constraint=False, default=1, on_delete=django.db.models.deletion.CASCADE, to='profiling.teeths'),
        ),
    ]

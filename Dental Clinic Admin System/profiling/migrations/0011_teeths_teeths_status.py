# Generated by Django 3.2.7 on 2021-09-28 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0010_alter_stock_in_item_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='teeths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LCI_left', models.CharField(default='Lower Central Incisor(Left)', max_length=200)),
                ('LLI_left', models.CharField(default='Lower Lateral Incisor(Left)', max_length=200)),
                ('LC_left', models.CharField(default='Lower Canine(Left)', max_length=200)),
                ('LF_left', models.CharField(default='Lower First Molar(Left)', max_length=200)),
                ('LSM_left', models.CharField(default='Lower Second Molar(Left)', max_length=200)),
                ('LCI_right', models.CharField(default='Lower Central Incisor(Right)', max_length=200)),
                ('LLI_right', models.CharField(default='Lower Lateral Incisor(Right)', max_length=200)),
                ('LC_right', models.CharField(default='Lower Canine(Right)', max_length=200)),
                ('LFM_right', models.CharField(default='Lower First Molar(Right)', max_length=200)),
                ('LSM_right', models.CharField(default='Lower Second Molar(Right)', max_length=200)),
                ('UCI_left', models.CharField(default='Upper Central Incisor(Left)', max_length=200)),
                ('ULI_left', models.CharField(default='Upper Lateral Incisor(Left)', max_length=200)),
                ('UC_left', models.CharField(default='Upper Canine(Left)', max_length=200)),
                ('UF_left', models.CharField(default='Upper First Molar(Left)', max_length=200)),
                ('USM_left', models.CharField(default='Upper Second Molar(Left)', max_length=200)),
                ('UCI_right', models.CharField(default='Upper Central Incisor(Right)', max_length=200)),
                ('ULI_right', models.CharField(default='Upper Lateral Incisor(Right)', max_length=200)),
                ('UC_right', models.CharField(default='Upper Canine(Right)', max_length=200)),
                ('UFM_right', models.CharField(default='Upper First Molar(Right)', max_length=200)),
                ('USM_right', models.CharField(default='Upper Second Molar(Right)', max_length=200)),
                ('patient_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiling.profile')),
            ],
        ),
        migrations.CreateModel(
            name='teeths_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('procedure_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiling.procedures_done')),
                ('teeth_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiling.teeths')),
            ],
        ),
    ]

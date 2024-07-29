# Generated by Django 5.0.7 on 2024-07-27 09:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('specialization', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=255)),
                ('sname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_no', models.CharField(max_length=10)),
                ('emergency_phone_no', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=255)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uid',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='emergency_phone_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('fname', models.CharField(max_length=255)),
                ('sname', models.CharField(max_length=255)),
                ('disease', models.JSONField(max_length=100)),
                ('time_duration', models.DurationField()),
                ('symptoms', models.JSONField(max_length=100)),
                ('causes_of_disease', models.JSONField(max_length=100)),
                ('allergy', models.JSONField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('slot_time', models.TimeField()),
                ('allocated_time', models.TimeField()),
                ('allocated_date', models.DateField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediapp.doctor')),
            ],
        ),
    ]

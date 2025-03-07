# Generated by Django 5.1.6 on 2025-03-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('autos_plate', models.CharField(max_length=7)),
                ('checkin_date', models.DateField(auto_now_add=True)),
                ('checkin_time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-checkin_time',),
            },
        ),
    ]

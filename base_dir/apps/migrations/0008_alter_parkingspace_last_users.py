# Generated by Django 5.1.6 on 2025-03-07 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_driver_monthly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspace',
            name='last_users',
            field=models.JSONField(null=True),
        ),
    ]

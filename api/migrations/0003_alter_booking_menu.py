# Generated by Django 5.1 on 2024-08-10 03:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.menu'),
        ),
    ]

# Generated by Django 5.1.1 on 2025-01-10 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_carorders_vehicle_type_alter_carorders_orderstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carorders',
            name='user',
        ),
        migrations.RemoveField(
            model_name='carorders',
            name='vehicle',
        ),
    ]

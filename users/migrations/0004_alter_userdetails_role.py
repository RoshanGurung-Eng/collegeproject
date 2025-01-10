# Generated by Django 5.1.1 on 2025-01-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userdetails_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default='admin', max_length=255),
        ),
    ]
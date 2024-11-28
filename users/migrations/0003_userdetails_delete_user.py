# Generated by Django 5.1.3 on 2024-11-28 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_address_user_date_of_birth_user_email_verified_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('role', models.CharField(default=1, max_length=255)),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('email_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-17 16:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField(null=True)),
                ('full_name', models.CharField(help_text='Required.', max_length=100, null=True)),
                ('birthdate', models.DateField(help_text='Format: yyyy-mm-dd', null=True)),
                ('contact_number', models.CharField(help_text="Phone number must be entered in the format: '+999999999'. Up to 15 characters allowed", max_length=15, null=True)),
                ('current_home_address', models.CharField(max_length=255, null=True)),
                ('emergency_contact', models.CharField(max_length=255, null=True)),
                ('emergency_contact_email', models.EmailField(help_text='Required. Use a valid email address.', max_length=255, null=True)),
                ('emergency_contact_number', models.CharField(help_text="Phone number must be entered in the format: '+999999999'. Up to 15 characters allowed", max_length=15, null=True)),
                ('record_with_info', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('record_without_info', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-18 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_full_name_profile_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-18 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_art'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='full_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='current_home_address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='emergency_contact',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='emergency_contact_email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='emergency_contact_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='record_with_info',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='record_without_info',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='input bio here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='commission_rates',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='commissions_open',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='genre',
            field=models.TextField(default='input art genre/style here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='is_artist',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='main.profile'),
        ),
    ]

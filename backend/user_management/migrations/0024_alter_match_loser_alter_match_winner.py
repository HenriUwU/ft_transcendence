# Generated by Django 5.0.2 on 2024-05-29 15:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0023_user_log2fa_user_log42api_usertwofactorauthdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='loser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lost_matches', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_matches', to=settings.AUTH_USER_MODEL),
        ),
    ]

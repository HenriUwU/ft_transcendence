# Generated by Django 5.0.2 on 2024-06-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0024_alter_match_loser_alter_match_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]

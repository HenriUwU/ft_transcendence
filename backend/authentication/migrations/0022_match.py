# Generated by Django 5.0.2 on 2024-04-22 12:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0021_alter_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=50)),
                ('match_date', models.DateTimeField(auto_now_add=True)),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lost_matches', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='won_matches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
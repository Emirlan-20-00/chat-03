# Generated by Django 5.1.4 on 2024-12-23 04:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0007_chat_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saveitem',
            old_name='save',
            new_name='items',
        ),
        migrations.RenameField(
            model_name='saveitem',
            old_name='post',
            new_name='save_items',
        ),
        migrations.AlterField(
            model_name='save',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='saves', to=settings.AUTH_USER_MODEL),
        ),
    ]

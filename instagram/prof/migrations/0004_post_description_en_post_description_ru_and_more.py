# Generated by Django 5.1.4 on 2024-12-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0003_alter_postlike_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtag_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtag_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

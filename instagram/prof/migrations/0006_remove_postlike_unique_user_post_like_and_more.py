# Generated by Django 5.1.4 on 2024-12-21 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0005_postlike_unique_user_post_like'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='postlike',
            name='unique_user_post_like',
        ),
        migrations.AlterUniqueTogether(
            name='commentlike',
            unique_together={('user', 'comment')},
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('follower', 'following')},
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together={('user', 'post')},
        ),
    ]

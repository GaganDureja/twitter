# Generated by Django 5.0.3 on 2024-07-06 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_alter_tweet_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='updated_at',
            new_name='last_edited_at',
        ),
    ]

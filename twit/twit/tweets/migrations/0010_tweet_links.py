# Generated by Django 2.0.7 on 2018-07-05 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0009_remove_tweet_tweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='links',
            field=models.URLField(null=True),
        ),
    ]
# Generated by Django 2.0.7 on 2018-07-04 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20180704_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commenttweet',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='commenttweet',
            name='tweet',
        ),
        migrations.DeleteModel(
            name='CommentTweet',
        ),
    ]

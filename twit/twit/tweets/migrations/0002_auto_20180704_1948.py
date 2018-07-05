# Generated by Django 2.0.7 on 2018-07-04 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='tweet',
        ),
        migrations.AddField(
            model_name='tweet',
            name='twit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to='tweets.Tweet'),
        ),
    ]

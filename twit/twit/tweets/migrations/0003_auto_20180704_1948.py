# Generated by Django 2.0.7 on 2018-07-04 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20180704_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='twit',
            new_name='tweet',
        ),
    ]
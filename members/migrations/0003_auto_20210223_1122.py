# Generated by Django 3.1.4 on 2021-02-23 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20210223_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='group_name',
        ),
    ]
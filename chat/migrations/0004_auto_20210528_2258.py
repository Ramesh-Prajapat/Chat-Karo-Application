# Generated by Django 2.2.1 on 2021-05-28 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20201101_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='dob',
        ),
    ]
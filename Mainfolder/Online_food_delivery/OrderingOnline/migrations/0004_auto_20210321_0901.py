# Generated by Django 3.1.5 on 2021-03-21 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant1', '0024_auto_20210321_0821'),
        ('OrderingOnline', '0003_notification'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='notification',
            new_name='alert',
        ),
    ]

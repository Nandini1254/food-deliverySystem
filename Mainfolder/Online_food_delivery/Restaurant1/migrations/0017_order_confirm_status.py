# Generated by Django 3.1.5 on 2021-03-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant1', '0016_auto_20210316_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_confirm',
            name='status',
            field=models.CharField(default='Ordered', max_length=15),
        ),
    ]

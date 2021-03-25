# Generated by Django 3.1.5 on 2021-03-18 19:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_boy', '0003_auto_20210319_0106'),
        ('Restaurant1', '0018_auto_20210318_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_confirm',
            name='delivery_boy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery_boy.deliveryboy'),
        ),
        migrations.AddField(
            model_name='order_confirm',
            name='delivery_charge',
            field=models.DecimalField(decimal_places=6, default=40.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order_confirm',
            name='creat_on',
            field=models.DateField(default=datetime.date(2021, 3, 19)),
        ),
    ]

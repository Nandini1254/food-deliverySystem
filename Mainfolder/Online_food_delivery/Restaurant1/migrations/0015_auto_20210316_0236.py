# Generated by Django 3.1.5 on 2021-03-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant1', '0014_order_confirm_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_confirm',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
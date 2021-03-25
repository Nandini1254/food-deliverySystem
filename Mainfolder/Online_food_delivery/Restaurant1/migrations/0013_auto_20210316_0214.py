# Generated by Django 3.1.5 on 2021-03-15 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant1', '0012_auto_20210316_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='feedback',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='offer',
            name='discount',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19),
        ),
    ]
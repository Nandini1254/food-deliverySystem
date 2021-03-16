# Generated by Django 3.1.5 on 2021-03-15 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant1', '0010_order_confirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_amount',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='discount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='item',
            name='feedback',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=6, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='total',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='offer',
            name='discount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='price',
            field=models.DecimalField(decimal_places=6, max_digits=6),
        ),
    ]

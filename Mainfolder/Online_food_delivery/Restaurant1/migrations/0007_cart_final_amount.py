# Generated by Django 3.1.5 on 2021-03-09 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant1', '0006_auto_20210308_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='final_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]

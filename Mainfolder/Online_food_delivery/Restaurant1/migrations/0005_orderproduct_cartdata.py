# Generated by Django 3.1.5 on 2021-03-13 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant1', '0004_restaurant_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='cartdata',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Restaurant1.cart'),
            preserve_default=False,
        ),
    ]

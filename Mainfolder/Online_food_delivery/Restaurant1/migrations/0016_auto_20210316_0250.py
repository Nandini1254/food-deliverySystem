# Generated by Django 3.1.5 on 2021-03-15 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrderingOnline', '0002_account_user'),
        ('Restaurant1', '0015_auto_20210316_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_confirm',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OrderingOnline.customer'),
        ),
        migrations.AlterField(
            model_name='order_confirm',
            name='Item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Restaurant1.item'),
        ),
    ]

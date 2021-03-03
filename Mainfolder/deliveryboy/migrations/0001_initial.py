# Generated by Django 3.0.4 on 2021-02-26 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deliveryboy_manager',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('deliveryboy_name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('uname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=6)),
            ],
        ),
    ]

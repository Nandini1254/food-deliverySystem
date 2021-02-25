# Generated by Django 3.1.5 on 2021-02-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurant_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='rname',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='restaurant_manager',
            name='Restaurant_photo',
            field=models.ImageField(upload_to='menu_images/'),
        ),
    ]
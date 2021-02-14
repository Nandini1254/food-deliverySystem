# Generated by Django 3.1.5 on 2021-02-14 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderingOnline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50)),
                ('pdesc', models.CharField(default='delicious', max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pimage', models.ImageField(upload_to='menu_images/')),
                ('category', models.ManyToManyField(related_name='item', to='OrderingOnline.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('items', models.ManyToManyField(blank=True, related_name='order', to='OrderingOnline.Item')),
            ],
        ),
    ]

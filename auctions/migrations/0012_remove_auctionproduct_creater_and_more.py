# Generated by Django 4.0.5 on 2022-07-02 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_auctionproduct_creater_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionproduct',
            name='creater',
        ),
        migrations.AlterField(
            model_name='auctionproduct',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 2, 17, 8, 30, 137849)),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-02 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auctionproduct_creator_alter_auctionproduct_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionproduct',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='auctionproduct',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 2, 17, 45, 6, 533449)),
        ),
    ]

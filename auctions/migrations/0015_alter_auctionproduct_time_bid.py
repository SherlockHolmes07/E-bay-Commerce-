# Generated by Django 4.0.5 on 2022-07-03 13:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_auctionproduct_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionproduct',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 13, 13, 56, 624684)),
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topBid', models.IntegerField()),
                ('time', models.DateTimeField(default=datetime.datetime(2022, 7, 3, 13, 13, 56, 624684))),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='u_bids', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.auctionproduct')),
            ],
        ),
    ]
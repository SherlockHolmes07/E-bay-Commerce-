# Generated by Django 4.0.5 on 2022-07-02 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auctionproduct_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionproduct',
            old_name='created_at',
            new_name='time',
        ),
    ]
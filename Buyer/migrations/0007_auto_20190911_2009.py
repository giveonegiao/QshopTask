# Generated by Django 2.1.8 on 2019-09-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0006_payorder_order_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payorder',
            name='order_count',
            field=models.IntegerField(default=0),
        ),
    ]

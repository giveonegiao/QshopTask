# Generated by Django 2.1.8 on 2019-09-11 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0007_auto_20190911_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payorder',
            name='order_count',
        ),
    ]

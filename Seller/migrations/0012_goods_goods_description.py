# Generated by Django 2.1.8 on 2019-09-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0011_auto_20190910_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_description',
            field=models.TextField(default='真香,好吃不贵'),
        ),
    ]

# Generated by Django 2.1.8 on 2019-09-09 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0003_remove_user_user_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

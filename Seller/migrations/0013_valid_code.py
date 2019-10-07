# Generated by Django 2.1.8 on 2019-09-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0012_goods_goods_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valid_Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_content', models.CharField(max_length=32)),
                ('code_user', models.EmailField(max_length=254)),
                ('code_time', models.DateTimeField(auto_now=True)),
                ('code_state', models.IntegerField(default=0)),
            ],
        ),
    ]
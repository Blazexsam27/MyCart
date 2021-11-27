# Generated by Django 3.2.8 on 2021-11-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('adId', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='shop/images')),
                ('adName', models.CharField(default='', max_length=256)),
                ('adDesc', models.CharField(default='', max_length=256)),
                ('pubDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

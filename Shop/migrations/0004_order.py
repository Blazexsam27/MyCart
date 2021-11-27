# Generated by Django 3.2.8 on 2021-10-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_auto_20211026_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=50)),
            ],
        ),
    ]

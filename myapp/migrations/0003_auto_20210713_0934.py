# Generated by Django 3.2.5 on 2021-07-13 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210713_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Discount_from_pricelist',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Final_price_USD',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Finalprice_of_Localcurrency',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='GLobal_price_listprice_USD',
            field=models.FloatField(max_length=200, null=True),
        ),
    ]

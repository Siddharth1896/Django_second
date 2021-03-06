# Generated by Django 3.2.5 on 2021-08-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210713_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Awarded',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Country',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Currency',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Date_of_entry',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Discount_from_pricelist',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Final_price_USD',
            field=models.FloatField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Finalprice_of_Localcurrency',
            field=models.FloatField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='GLobal_price_listprice_USD',
            field=models.FloatField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Part_number',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Process_number',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Quantity',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Volume_of_Deal',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]

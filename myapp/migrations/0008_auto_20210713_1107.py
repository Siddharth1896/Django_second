# Generated by Django 3.2.5 on 2021-07-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20210713_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='data',
            name='Date_of_entry',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

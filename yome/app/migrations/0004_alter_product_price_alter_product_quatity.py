# Generated by Django 4.0.4 on 2022-06-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_quatity_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='quatity',
            field=models.IntegerField(default=2),
        ),
    ]

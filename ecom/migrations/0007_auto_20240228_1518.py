# Generated by Django 3.0.5 on 2024-02-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_auto_20240228_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
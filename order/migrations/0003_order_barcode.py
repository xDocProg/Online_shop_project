# Generated by Django 5.0.7 on 2024-08-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='barcode',
            field=models.ImageField(blank=True, null=True, upload_to='barcodes/'),
        ),
    ]
